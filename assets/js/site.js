(() => {
'use strict';
const menuButton=document.querySelector('.menu-toggle'),nav=document.querySelector('#site-nav');
if(menuButton&&nav){
 menuButton.hidden=false;document.documentElement.classList.add('js-ready');
 const close=()=>{nav.classList.remove('is-open');menuButton.setAttribute('aria-expanded','false');};
 menuButton.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));nav.classList.toggle('is-open',open);});
 nav.addEventListener('click',e=>{if(e.target.closest('a'))close();});
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('is-open')){close();menuButton.focus();}});
 window.matchMedia('(min-width:821px)').addEventListener('change',close);
}
document.querySelectorAll('.focus-explorer').forEach(explorer=>{
 const control=explorer.querySelector('.focus-control'),range=explorer.querySelector('input'),output=explorer.querySelector('output');
 if(!control||!range||!output)return;
 control.hidden=false;
 range.addEventListener('input',()=>{explorer.dataset.layer=range.value;output.value=range.value.padStart(2,'0')+' / 05';range.setAttribute('aria-valuetext','Conceptual focus position '+range.value+' of 5');});
});
const filters=document.querySelector('.filter-group');
if(filters){
 filters.hidden=false;
 const items=[...document.querySelectorAll('.publication')],result=document.querySelector('.results-status');
 const update=filter=>{let count=0;items.forEach(item=>{const shown=filter==='all'||item.dataset.first==='true';item.hidden=!shown;if(shown)count++;});filters.querySelectorAll('button').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.filter===filter)));result.textContent='Showing '+count+' publications';};
 filters.addEventListener('click',e=>{const button=e.target.closest('button');if(button)update(button.dataset.filter);});update('all');
}
})();