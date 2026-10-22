"""Write stripped CSVs (one per worksheet) for the native spreadsheets of set 25 (IDL).

Usage: python3 -I data/_tools/idl_strip.py data/sources/25_idl_shipper_freight_files data/derived/idl \
           <comma-separated IDL ids whose sheets hold consumer (B2C) rows>
Needs openpyxl and xlrd. Rules: data/derived/idl/STRIPPED.md (collector K2, check BE).
The five *__stripped.zip files are already stripped; their residual address/phone cells were blanked by hand.
"""
import sys,os,re,csv,json
import warnings
warnings.filterwarnings('ignore')
import openpyxl, xlrd
SRC, OUT = sys.argv[1], sys.argv[2]
EM=re.compile(r'[\w.+-]+@[\w-]+(\.[\w-]+)+')
PHONE=re.compile(r'(?<!\d)(\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4})(?!\d)')
DROP=re.compile(r'(\bprepared by\b|\bpreparer\b|\bcreated ?by\b|\bmodified by\b|\bchanged by\b|\bentered by\b|\brequest(e|o)r\b|\brequisitioner\b|\bapprover\b|^approved by\s*:?$|\bsigner\b|\bsignature\b|\bsigned by\b|\bcontact\b|\bbuyer\b|\bplanner\b|\battention\b|\battn\b|e-?mail|\bphone\b|\bfax\b|\bpod name\b|\bemployee\b|^user\b|\buser ?(id|name)\b|\bowner\b|\breviewer\b|\bcoordinator\b|\bdriver\b|\bpicked by\b|\bchecked by\b|\bprocessed by\b|\binspector\b|\bperformed by\b|\bsalesperson\b|\bsales ?rep\b|\bslsrep\b|^rep$|\bcustodian\b|^author$|\bsubmitted by\b|\blogged by\b|\bassigned to\b|\banalyst\b|\baddress|\baddr\d|^au$|person responsible|process owner|\\bfirst ?name\\b|\\blast ?name\\b|\\bsurname\\b)',re.I)
# B2C person-name columns (JUUL DCL detail sheets): consumer names
B2CNAME=re.compile(r'^(company|ship ?to ?company|shiptocompany|ship to customer|ship to name|customer name|name|consignee name|bill to company|bill to name|ship to attention)$',re.I)
log=[]
LABEL=re.compile(r'^\s*(user|prepared by|preparer|reviewed by|reviewer|approved by|approver|created by|modified by|last modified by|owner|process owner|person responsible( for process)?|signed|signature|requested by|requester|submitted by|contact|attn|attention|buyer|planner|analyst|sign-?off)\b.*:?\s*(/\s*date\s*:?)?\s*$',re.I)
UID=re.compile(r'^(?=.{5,40}$)[A-Za-z][a-z]+[._][A-Za-z][A-Za-z\-]+$')
EXT=re.compile(r'\.(xlsx?|xlsm|csv|pdf|docx?|txt|com|net|org)$',re.I)
def hdr_idx(rows):
    best=0;bs=-1
    for k,r in enumerate(rows[:20]):
        sc=sum(1 for c in r if isinstance(c,str) and c.strip() and not re.match(r'^[-\d.,$%() ]+$',c.strip()))
        if sc>bs: best,bs=k,sc
    return best
def clean(v):
    if v is None: return ''
    s=str(v)
    if EM.search(s): s=EM.sub('',s)
    if isinstance(v,str) and PHONE.search(s): s=PHONE.sub('',s)
    return s
def process(id_,path,sheet,rowiter,b2c):
    import itertools
    head=[]
    for r in rowiter:
        head.append(list(r))
        if len(head)>=20: break
    if not head or not any(any(c not in (None,'') for c in r) for r in head): return
    k=hdr_idx(head); h=[str(c).strip() if c is not None else '' for c in head[k]]
    drop=set(); why={}
    for hr in head[:k+1]:
        for j,c in enumerate(hr):
            c=str(c).strip() if c is not None else ''
            if len(c)>60: continue
            if c and DROP.search(c) and not EM.search(c): drop.add(j); why.setdefault(j,c)
            if b2c and c and B2CNAME.match(c): drop.add(j); why.setdefault(j,c)
            if c and EM.search(c): drop.add(j); why.setdefault(j,'[header cell was an email address]')
    h=h+['']*(max(drop|{0})+1-len(h)) if drop else h
    safe=re.sub(r'[^A-Za-z0-9._-]+','_',sheet)[:60]
    out=os.path.join(OUT,'%s__%s.csv'%(id_,safe))
    if os.path.exists(out): out=out[:-4]+'_%d.csv'%len(log)
    blanked=0; n=0
    with open(out,'w',newline='') as f:
        w=csv.writer(f)
        below=set()
        for r in itertools.chain(head,rowiter):
            n+=1; row=[]; r=list(r); nxt=set()
            for j,c in enumerate(r):
                cs=str(c).strip() if c is not None else ''
                if cs and len(cs)<50 and LABEL.match(cs):
                    for t in (j+1,j+2,j+3):
                        if t<len(r) and r[t] not in (None,''): r[t]=''; blanked+=1
                    nxt.add(j); nxt.add(j+1)
            for j in below:
                if j<len(r) and r[j] not in (None,'') and isinstance(r[j],str) and not LABEL.match(r[j]): r[j]=''; blanked+=1
            below=nxt
            for j,c in enumerate(r):
                if j in drop: continue
                v=clean(c)
                if isinstance(c,str) and UID.match(c.strip()) and not EXT.search(c.strip()): v=''
                if v!=(str(c) if c is not None else ''): blanked+=1
                row.append(v)
            w.writerow(row)
    log.append((id_,os.path.basename(path),sheet,os.path.basename(out),n,[why[j] for j in sorted(drop)],blanked))
def run(b2c_ids):
    for fn in sorted(os.listdir(SRC)):
            id_=fn.split('__')[0]
            p=os.path.join(SRC,fn); ext=fn.lower().rsplit('.',1)[-1]
            b2c=id_ in b2c_ids
            try:
                if ext in ('xlsx','xlsm'):
                    wb=openpyxl.load_workbook(p,read_only=True,data_only=True)
                    for ws in wb.worksheets:
                        process(id_,p,ws.title,ws.iter_rows(values_only=True),b2c)
                elif ext=='xls':
                    wb=xlrd.open_workbook(p,on_demand=True)
                    for sh in wb.sheets():
                        process(id_,p,sh.name,(sh.row_values(i) for i in range(sh.nrows)),b2c)
                elif ext=='csv':
                    process(id_,p,'csv',csv.reader(open(p,encoding='utf-8',errors='replace')),b2c)
            except Exception as e:
                log.append((id_,fn,'ERROR',str(e)[:120],0,[],0))
    for l in log: print(l[0],l[2][:30],l[4],l[5][:8],l[6])
os.makedirs(OUT, exist_ok=True)
run(set(sys.argv[3].split(',')) if len(sys.argv) > 3 else set())
