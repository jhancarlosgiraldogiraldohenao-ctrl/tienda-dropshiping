const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async()=>{
  const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
  const p=await b.newPage();
  await p.goto('file://'+process.cwd()+'/plan.html',{waitUntil:'networkidle'});
  await p.evaluate(()=>document.fonts.ready);
  await p.pdf({path:process.argv[2],format:'A4',printBackground:true,displayHeaderFooter:true,headerTemplate:'<span></span>',
    footerTemplate:'<div style="font-size:7px;color:#6E5F56;width:100%;text-align:center;font-family:sans-serif">Soy Toffee · El viaje de Toffee · Sección 1 · <span class="pageNumber"></span>/<span class="totalPages"></span></div>',
    margin:{top:'14mm',bottom:'16mm',left:'13mm',right:'13mm'}});
  await b.close();
})();
