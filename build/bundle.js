var app=function(){"use strict";function t(){}function e(t){return t()}function n(){return Object.create(null)}function o(t){t.forEach(e)}function r(t){return"function"==typeof t}function c(t,e){return t!=t?e==e:t!==e||t&&"object"==typeof t||"function"==typeof t}function u(t,e){t.appendChild(e)}function s(t,e,n){t.insertBefore(e,n||null)}function i(t){t.parentNode.removeChild(t)}function l(t){return document.createElement(t)}function a(t){return document.createTextNode(t)}function f(){return a(" ")}function p(t,e,n,o){return t.addEventListener(e,n,o),()=>t.removeEventListener(e,n,o)}function d(t,e,n){null==n?t.removeAttribute(e):t.getAttribute(e)!==n&&t.setAttribute(e,n)}function $(t,e){e=""+e,t.wholeText!==e&&(t.data=e)}let h;function m(t){h=t}const g=[],b=[],x=[],y=[],v=Promise.resolve();let _=!1;function k(t){x.push(t)}let w=!1;const j=new Set;function A(){if(!w){w=!0;do{for(let t=0;t<g.length;t+=1){const e=g[t];m(e),E(e.$$)}for(m(null),g.length=0;b.length;)b.pop()();for(let t=0;t<x.length;t+=1){const e=x[t];j.has(e)||(j.add(e),e())}x.length=0}while(g.length);for(;y.length;)y.pop()();_=!1,w=!1,j.clear()}}function E(t){if(null!==t.fragment){t.update(),o(t.before_update);const e=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,e),t.after_update.forEach(k)}}const C=new Set;function B(t,e){t&&t.i&&(C.delete(t),t.i(e))}function S(t,e,n,o){if(t&&t.o){if(C.has(t))return;C.add(t),undefined.c.push((()=>{C.delete(t),o&&(n&&t.d(1),o())})),t.o(e)}}function T(t){t&&t.c()}function H(t,n,c,u){const{fragment:s,on_mount:i,on_destroy:l,after_update:a}=t.$$;s&&s.m(n,c),u||k((()=>{const n=i.map(e).filter(r);l?l.push(...n):o(n),t.$$.on_mount=[]})),a.forEach(k)}function L(t,e){const n=t.$$;null!==n.fragment&&(o(n.on_destroy),n.fragment&&n.fragment.d(e),n.on_destroy=n.fragment=null,n.ctx=[])}function N(t,e){-1===t.$$.dirty[0]&&(g.push(t),_||(_=!0,v.then(A)),t.$$.dirty.fill(0)),t.$$.dirty[e/31|0]|=1<<e%31}function O(e,r,c,u,s,l,a,f=[-1]){const p=h;m(e);const d=e.$$={fragment:null,ctx:null,props:l,update:t,not_equal:s,bound:n(),on_mount:[],on_destroy:[],on_disconnect:[],before_update:[],after_update:[],context:new Map(r.context||(p?p.$$.context:[])),callbacks:n(),dirty:f,skip_bound:!1,root:r.target||p.$$.root};a&&a(d.root);let $=!1;if(d.ctx=c?c(e,r.props||{},((t,n,...o)=>{const r=o.length?o[0]:n;return d.ctx&&s(d.ctx[t],d.ctx[t]=r)&&(!d.skip_bound&&d.bound[t]&&d.bound[t](r),$&&N(e,t)),n})):[],d.update(),$=!0,o(d.before_update),d.fragment=!!u&&u(d.ctx),r.target){if(r.hydrate){const t=function(t){return Array.from(t.childNodes)}(r.target);d.fragment&&d.fragment.l(t),t.forEach(i)}else d.fragment&&d.fragment.c();r.intro&&B(e.$$.fragment),H(e,r.target,r.anchor,r.customElement),A()}m(p)}class M{$destroy(){L(this,1),this.$destroy=t}$on(t,e){const n=this.$$.callbacks[t]||(this.$$.callbacks[t]=[]);return n.push(e),()=>{const t=n.indexOf(e);-1!==t&&n.splice(t,1)}}$set(t){var e;this.$$set&&(e=t,0!==Object.keys(e).length)&&(this.$$.skip_bound=!0,this.$$set(t),this.$$.skip_bound=!1)}}function P(e){let n,o,r,c,p,d;return{c(){n=l("p"),n.textContent="Hello from nested.svelte",o=f(),r=l("p"),c=a("This has a "),p=a(e[0]),d=a(" property")},m(t,e){s(t,n,e),s(t,o,e),s(t,r,e),u(r,c),u(r,p),u(r,d)},p(t,[e]){1&e&&$(p,t[0])},i:t,o:t,d(t){t&&i(n),t&&i(o),t&&i(r)}}}function q(t,e,n){let{prop:o}=e;return t.$$set=t=>{"prop"in t&&n(0,o=t.prop)},[o]}class V extends M{constructor(t){super(),O(this,t,q,P,c,{prop:0})}}function z(e){let n,o,r;return{c(){n=l("button"),n.textContent="Add to B"},m(t,c){s(t,n,c),o||(r=p(n,"click",e[5]),o=!0)},p:t,d(t){t&&i(n),o=!1,r()}}}function D(t){let e,n,r,c,h,m,g,b,x,y,v,_,k,w,j,A,E,C,N,O,M,P,q,D,F,G,I,J,K,Q,R,U=t[1]>t[3].length&&z(t);return g=new V({props:{prop:1234}}),J=new V({props:{prop:"new text"}}),{c(){e=l("main"),n=l("button"),n.textContent="Add to A",r=f(),U&&U.c(),c=f(),h=l("button"),h.textContent="Push to list",m=f(),T(g.$$.fragment),b=f(),x=l("p"),y=a("list: "),v=a(t[3]),_=f(),k=l("h1"),w=a("Hello "),j=a(t[0]),A=a("!"),E=f(),C=l("p"),C.innerHTML='Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn\n\t\thow to build Svelte apps.',N=f(),O=l("p"),M=a("A is "),P=a(t[1]),q=f(),D=l("p"),F=a("B is "),G=a(t[2]),I=f(),T(J.$$.fragment),d(x,"class","svelte-1ic1je1"),d(k,"class","svelte-1ic1je1"),d(C,"class","svelte-1ic1je1"),d(O,"class","svelte-1ic1je1"),d(D,"class","svelte-1ic1je1"),d(e,"class","svelte-1ic1je1")},m(o,i){s(o,e,i),u(e,n),u(e,r),U&&U.m(e,null),u(e,c),u(e,h),u(e,m),H(g,e,null),u(e,b),u(e,x),u(x,y),u(x,v),u(e,_),u(e,k),u(k,w),u(k,j),u(k,A),u(e,E),u(e,C),u(e,N),u(e,O),u(O,M),u(O,P),u(e,q),u(e,D),u(D,F),u(D,G),u(e,I),H(J,e,null),K=!0,Q||(R=[p(n,"click",t[4]),p(h,"click",t[6])],Q=!0)},p(t,[n]){t[1]>t[3].length?U?U.p(t,n):(U=z(t),U.c(),U.m(e,c)):U&&(U.d(1),U=null),(!K||8&n)&&$(v,t[3]),(!K||1&n)&&$(j,t[0]),(!K||2&n)&&$(P,t[1]),(!K||4&n)&&$(G,t[2])},i(t){K||(B(g.$$.fragment,t),B(J.$$.fragment,t),K=!0)},o(t){S(g.$$.fragment,t),S(J.$$.fragment,t),K=!1},d(t){t&&i(e),U&&U.d(),L(g),L(J),Q=!1,o(R)}}}function F(t,e,n){let{name:o}=e,r=1,c=1,u=[];return t.$$set=t=>{"name"in t&&n(0,o=t.name)},t.$$.update=()=>{6&t.$$.dirty&&console.log(`countA is ${r}\n countB is ${c}`)},[o,r,c,u,function(){n(1,r+=1)},function(){n(2,c+=1)},function(){n(3,u[u.length]=" "+(u.length+1),u),n(3,u[u.length]=" "+(u.length+1),u),n(3,u=u.slice(1))}]}return new class extends M{constructor(t){super(),O(this,t,F,D,c,{name:0})}}({target:document.body,props:{name:"world"}})}();
//# sourceMappingURL=bundle.js.map
