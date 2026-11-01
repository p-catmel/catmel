let builds = null;
let upgrads = null;
let money = 0;
let mps = 0;
let mpc = 1;
const showbuilds = document.getElementById('showbuilds')
if(document.cookie){
    console.log("temp");
}
else{
    builds = [
        {name:"cursor",cost:15,owned:0,mpb:1,pow:1},
        {name:"laborer",cost:100,owned:0,mpb:15,pow:1}
    ];
}
function updatemps(builds){
    mps = 0;
    builds.forEach((b,i) => {
        mps += (b.mpb * b.pow * b.owned);
    })
}
showbuilds.addEventListener('click',(e) => {
    if(e.target.tagName == "BUTTON"){
        const targetindex = e.target.dataset.index
        const t = builds[targetindex];
        const name = t['name']
        const cost = t['cost']
        if(money >= cost){
            money -= cost;
            builds[targetindex].owned += 1;
            builds[targetindex].cost = Math.ceil(builds[targetindex].cost *= 1.1);
            e.target.textContent = `${name} 価格:${builds[targetindex].cost}`;
            updatemps(builds);
            show();
        }
    }
});
function gb(builds){
    builds.forEach((b,i) => {
        g = document.createElement('button');
        g.textContent = `${b.name} 価格:${b.cost}`;
        g.className = b.name;
        g.dataset.index = i;
        showbuilds.appendChild(g);
    });
}
function show(){
    showmoney = document.getElementById('showmoney');
    showmps = document.getElementById('showmps');
    showmpc = document.getElementById('showmpc');
    showmoney.textContent = `所持金:${money}`;
    showmps.textContent = `mps:${mps}`;
    showmpc.textContent = `mpc:${mpc}`;
}
function clicked(mpc){
    money += mpc;
    show()
}
function increase(mps){
    money += mps;
}
setInterval(() => {
    increase(mps);
    show();
}, 1000);
gb(builds);