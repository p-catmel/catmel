let builds = null;
let upgrads = null;
let money = 0;
let mps = 0;
let mpc = 1;
if(document.cookie){
    console.log("temp");
}
else{
    builds = [
        {name:"cursor",cost:15,owned:0},
        {name:"laborer",cost:100,owned:0}
    ];
}
function gb(builds){
    showbuilds = document.getElementById('showbuilds');
    builds.forEach(b => {
        g = document.createElement('button');
        g.textContent = b.name;
        g.className = b.name;
        showbuilds.appendChild(g);
    });
}
function show(money,mpc,mps){
    showmoney = document.getElementById('showmoney');
    showmps = document.getElementById('showmps');
    showmpc = document.getElementById('showmpc');
    showmoney.textContent = `所持金:${money}`;
    showmps.textContent = `mps:${mps}`;
    showmpc.textContent = `mpc:${mpc}`;
}
function clicked(mpc){
    money += mpc;
    show(money,mpc,mps)
}
setInterval(() => {
    show(money,mpc,mps);
}, 1000);
gb(builds);