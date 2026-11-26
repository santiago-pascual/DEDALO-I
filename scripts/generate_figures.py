"""Deterministic, dependency-free SVGs from published aggregate evidence."""
from pathlib import Path
from html import escape
import argparse
ROOT = Path(__file__).resolve().parents[1]

def diagram(title, subtitle, rows):
    w=960; h=125+len(rows)*79
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">', '<rect width="100%" height="100%" fill="#f8fafc"/>', '<g font-family="Arial, sans-serif">', f'<text x="32" y="40" font-size="25" font-weight="bold" fill="#14283e">{escape(title)}</text>',f'<text x="32" y="67" font-size="14" fill="#475569">{escape(subtitle)}</text>']
    for i,(a,b) in enumerate(rows):
        y=88+i*79
        s += [f'<rect x="32" y="{y}" width="896" height="65" rx="5" fill="white" stroke="#cbd5e1"/>',f'<rect x="32" y="{y}" width="5" height="65" fill="#32738b"/>',f'<text x="50" y="{y+25}" font-size="17" font-weight="bold" fill="#14283e">{escape(a)}</text>',f'<text x="50" y="{y+47}" font-size="14" fill="#475569">{escape(b)}</text>']
    return '\n'.join(s+['</g></svg>',''])

def summary():
    s=['<svg xmlns="http://www.w3.org/2000/svg" width="960" height="460" viewBox="0 0 960 460">','<rect width="960" height="460" fill="#f8fafc"/>','<g font-family="Arial, sans-serif" fill="#14283e">','<text x="32" y="40" font-size="25" font-weight="bold">P4 | Frozen historical research</text>','<text x="32" y="65" font-size="14">2020-06-23 to 2026-06-19 · Archived reference, not forward performance</text>']
    for i,(a,b) in enumerate([('Total R','+289.66R'),('Expectancy','+0.08899R'),('Profit factor','1.216'),('Win rate','50.66%'),('Max drawdown','−18.09R'),('Trades','3,255')]):
        x=32+i%3*300;y=85+i//3*76
        s += [f'<rect x="{x}" y="{y}" width="280" height="64" rx="4" fill="white" stroke="#cbd5e1"/>',f'<text x="{x+12}" y="{y+20}" font-size="13">{a}</text>',f'<text x="{x+12}" y="{y+48}" font-size="23" font-weight="bold">{b}</text>']
    for i,(a,b) in enumerate([('MRL1',430),('MRS2',863),('S2R',520),('ORB',1442)]):
        y=258+i*39;w=b/1442*620
        s += [f'<text x="32" y="{y+18}" font-size="15">{a}</text>',f'<rect x="120" y="{y}" width="{w:.2f}" height="23" fill="#32738b"/>',f'<text x="{132+w:.2f}" y="{y+17}" font-size="14">{b:,}</text>']
    return '\n'.join(s+['<text x="32" y="440" font-size="13">Counts measure frequency, not profit contribution. Full portfolio inputs absent.</text>','</g></svg>',''])

FIGURES={
'portfolio_evolution.svg':diagram('Portfolio evolution','Research configurations and forward operation are separate evidence sets.', [('P4 | Frozen research','MRL1 · MRS2 · S2R · ORB'),('P5 | Expanded research','P4 plus NBM-B; revised matched comparison reported'),('P5-R2 | Revised historical research','October matched report; November extended 3,858-trade reference'),('Forward Paper | Separate causal simulation','No verified current ledger or deployment identity in public release')]),
'system_architecture.svg':diagram('System architecture','Conceptual documented boundaries; deployment not independently verified.', [('01  Market-data ingestion','Historical and observed inputs; separate provenance'),('02  Temporal validation','Chronology, quality and session coverage'),('03  Feature generation and regime inference','Completed observations and forward-only filtering'),('04  Strategy decisions','Independent state; signal is not execution'),('05  Portfolio risk','Admission, exposure and account constraints'),('06  Simulated execution','Internal fills and modeled costs'),('07  Durable state and recovery','Checkpointing, reconciliation and fail-closed boundaries'),('08  Monitoring and analytics','Read-only diagnostics; frozen artifacts enter analytics separately')]),
'evidence_hierarchy.svg':diagram('Scientific evidence hierarchy','Evidence categories are complementary; no automatic progression is implied.', [('Archived results | Available','P4 and P5-R2 report aggregates; full tapes absent'),('Artifact reconciliation | Partial','S2R prior aggregation reported; P4 full reproduction pending'),('Execution replay | Reported','Frozen replay not rerun in public showcase'),('End-to-end causal validation | Incomplete','Matched P5 report recovered; independent full refit and native equivalence open'),('Forward Paper | Unverified here','No approved current ledger'),('Economic feasibility | Conditional','Conditional calendar overlay; evidence does not support real-money commitment')]),
'p4_summary.svg':summary(),
'economic_methodology.svg':diagram('Economic feasibility methodology','Archived conditional framework, not a forecast or native-fill simulation.', [('01  Historical strategy outcome profiles','Reconstructed P5-R2 inputs'),('02  Execution-cost assumptions','Adverse execution stress and modeled fees'),('03  Dependence-aware bootstrap','Shared stationary-block session paths'),('04  Account lifecycle simulation','Evaluation, loss constraints, replacement and activation'),('05  Fees and payout constraints','Distinguish account balance from cash withdrawals'),('06  Net economic outcomes','Distribution and downside; historical holiday-rule equivalence unverified')])}


# Aggregate transcription from October 28 certification and November 24/25 reports.
# No trade tape or production configuration is embedded in these figures.
def canvas(title, subtitle, height):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}">','<rect width="100%" height="100%" fill="#f8fafc"/>','<g font-family="Arial, sans-serif" fill="#14283e">',f'<text x="32" y="39" font-size="25" font-weight="bold">{escape(title)}</text>',f'<text x="32" y="66" font-size="14" fill="#475569">{escape(subtitle)}</text>']

def finish(s):
    return '\n'.join(s+['</g></svg>',''])

def matched():
    s=canvas('Matched portfolio comparison | P4-R2 vs P5-R2','963 eligible entry dates · 2021-05-06 to 2026-06-16 · historical simulated net USD',390)
    for i,(label,v4,v5) in enumerate([('Strict research sizing',6231.98,12660.98),('Adaptive research sizing',19239.20,28277.92)]):
        y=110+i*125
        s += [f'<text x="32" y="{y}" font-size="17" font-weight="bold">{label}</text>']
        for j,(name,v,color) in enumerate([('P4-R2',v4,'#64748b'),('P5-R2',v5,'#32738b')]):
            yy=y+17+j*33; w=v/30000*630
            s += [f'<text x="32" y="{yy+17}" font-size="14">{name}</text>',f'<rect x="130" y="{yy}" width="{w:.2f}" height="23" fill="{color}"/>',f'<text x="{140+w:.2f}" y="{yy+17}" font-size="14">${v:,.2f}</text>']
    s += ['<text x="32" y="370" font-size="13">Source: October final historical certification. Report-level evidence; not a new backtest or deployment certificate.</text>']
    return finish(s)

def extended():
    s=canvas('P5-R2 | Extended historical reference','2021-05-06 to 2026-10-07 · reconstructed trades · pinned signals',280)
    for i,(a,b) in enumerate([('Reconstructed trades','3,858'),('Gross simulated P&amp;L','$42,147'),('Modeled trading costs','$7,254'),('Net simulated P&amp;L','$34,893')]):
        x=32+i%2*460;y=85+i//2*77
        s += [f'<rect x="{x}" y="{y}" width="436" height="65" rx="4" fill="white" stroke="#cbd5e1"/>',f'<text x="{x+13}" y="{y+21}" font-size="14">{a}</text>',f'<text x="{x+13}" y="{y+49}" font-size="25" font-weight="bold">{b}</text>']
    s += ['<text x="32" y="265" font-size="13">November reports; zero added slippage. Not native fills, funded-account income or current Paper equity.</text>']
    return finish(s)

def dependence():
    s=canvas('NBM-B | Daily P&amp;L correlation'.replace('&amp;','&'),'October matched report · sample correlation with P4-R2 and each component',365)
    labels=['MRL1','MRS2','S2R','ORB','P4-R2']; vals=[[.010,-.002,-.025,.075,.025],[.021,-.062,-.017,.197,.144]]
    s += ['<text x="305" y="104" font-size="15" font-weight="bold">Strict</text>','<text x="610" y="104" font-size="15" font-weight="bold">Adaptive</text>']
    for i,label in enumerate(labels):
        y=120+i*40;s += [f'<text x="35" y="{y+23}" font-size="16">{label}</text>']
        for j in range(2):
            v=vals[j][i];x=250+j*305;op=abs(v)/.20*.7+.08
            color='#32738b' if v>=0 else '#a65b43'
            s += [f'<rect x="{x}" y="{y}" width="215" height="32" rx="3" fill="{color}" fill-opacity="{op:.3f}"/>',f'<text x="{x+107}" y="{y+22}" text-anchor="middle" font-size="16">{v:+.3f}</text>']
    s += ['<text x="32" y="349" font-size="13">Small historical correlations do not establish independence, future diversification or tail protection.</text>']
    return finish(s)

def uncertainty():
    s=canvas('Paired bootstrap | Incremental daily P&amp;L'.replace('&amp;','&'),'Full accounting clock (1,326 observations) · 95% percentile intervals · USD/day',440)
    names=['IID','Moving 5','Moving 10','Moving 20','Stationary 10']; data=[[(4.8644,1.9321,7.8918),(4.9589,2.0807,7.9126),(5.0134,2.0515,8.0717),(4.9922,1.9027,8.0656),(4.8217,1.7274,7.9073)],[(6.8181,2.6719,11.0924),(6.9548,2.8894,11.0543),(6.9909,2.9461,11.1119),(6.9652,2.9187,10.8814),(6.7770,2.7000,10.8153)]]
    x=lambda v: 180+v*58
    for tick in range(0,13,2):
        xx=x(tick);s += [f'<line x1="{xx}" y1="110" x2="{xx}" y2="365" stroke="#cbd5e1"/>',f'<text x="{xx}" y="387" text-anchor="middle" font-size="13">{tick}</text>']
    for i,name in enumerate(names):
        y=130+i*52;s += [f'<text x="32" y="{y+5}" font-size="14">{name}</text>']
        for j,color in enumerate(['#64748b','#32738b']):
            m,lo,hi=data[j][i]; yy=y-7+j*15
            s += [f'<line x1="{x(lo):.2f}" y1="{yy}" x2="{x(hi):.2f}" y2="{yy}" stroke="{color}" stroke-width="3"/>',f'<circle cx="{x(m):.2f}" cy="{yy}" r="5" fill="{color}"/>']
    s += ['<text x="32" y="94" font-size="13" fill="#64748b">● Strict</text>','<text x="110" y="94" font-size="13" fill="#32738b">● Adaptive</text>','<text x="32" y="420" font-size="13">10,000 draws per method and policy; historical selection and structural uncertainty remain.</text>']
    return finish(s)

def stress():
    s=canvas('Execution stress | Matched portfolio net P&amp;L'.replace('&amp;','&'),'October certification · added adverse ticks per market side · simulated net USD',495)
    series=[('Strict P4-R2','#8a98a8',[6231.98,3229.36,-171.86,-2819.30,-5313.96,-8388.58,-10250.42,-14503.90,-17947.62]),('Strict P5-R2','#32738b',[12660.98,9150.86,5217.14,1593.70,-1523.96,-5142.58,-7526.92,-12411.40,-16554.12]),('Adaptive P4-R2','#9b7059',[19239.20,14598.64,11011.70,7252.76,4569.60,1231.76,-1104.74,-5521.88,-8968.16]),('Adaptive P5-R2','#214762',[28277.92,23099.86,18967.92,14219.48,10884.32,6809.48,3791.98,-1416.66,-5841.94])]
    x=lambda i:105+95*i; y=lambda v:100+(30000-v)/50000*300
    for t in range(-20000,30001,10000):
        yy=y(t);s += [f'<line x1="105" y1="{yy}" x2="865" y2="{yy}" stroke="{"#14283e" if t==0 else "#cbd5e1"}"/>',f'<text x="94" y="{yy+5}" text-anchor="end" font-size="13">{t/1000:.0f}k</text>']
    for i in range(9):s += [f'<text x="{x(i)}" y="425" text-anchor="middle" font-size="13">{i}</text>']
    for j,(label,color,vs) in enumerate(series):
        points=' '.join(f'{x(i)},{y(v):.2f}' for i,v in enumerate(vs));dash=' stroke-dasharray="6 4"' if j%2==0 else ''
        s += [f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="3"{dash}/>']
        for i,v in enumerate(vs):s += [f'<circle cx="{x(i)}" cy="{y(v):.2f}" r="3" fill="{color}"/>']
        s += [f'<text x="{32+j*230}" y="454" font-size="13" fill="{color}">● {label}</text>']
    s += ['<text x="32" y="480" font-size="13">Zero = reference; stressed paths recompute admissions. Hypothetical slippage, not native-fill calibration.</text>']
    return finish(s)

FIGURES.update({'p5_matched_comparison.svg':matched(),'p5_extended_reference.svg':extended(),'nbm_dependence.svg':dependence(),'nbm_paired_uncertainty.svg':uncertainty(),'p5_slippage_stress.svg':stress()})

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    for name, content in FIGURES.items():
        p=ROOT/'figures'/name
        if args.check:
            if p.read_bytes()!=content.encode('utf-8'): raise SystemExit(f'Figure mismatch: {name}')
        else: p.write_bytes(content.encode('utf-8'))
    print(f'{len(FIGURES)} figures verified' if args.check else f'{len(FIGURES)} figures generated')
if __name__=='__main__': main()
