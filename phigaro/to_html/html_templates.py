header = '''<html>
  <head>
  <title>Phigaro report: {0}</title>
  <link rel="shortcut icon" href="https://pollytikhonova.github.io/phigaro/dna.png" />
  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" rel="stylesheet"/>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/bobeobibo/phigaro/scripts/FileSaver.min.js"></script>
  <script src="https://getbootstrap.com/docs/4.0/assets/js/vendor/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"></script>
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script> '''
style_css = '''
<style type="text/css">
  .container {
      max-width: 95vw;
  }
  .col, .col-1, .col-10, .col-11, .col-12, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-auto, .col-lg, .col-lg-1, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-auto, .col-md, .col-md-1, .col-md-10, .col-md-11, .col-md-12, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-auto, .col-sm, .col-sm-1, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-auto, .col-xl, .col-xl-1, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-auto {
    padding: 0px;
  }
  thead {
      background-color: white;
  }
  .table thead th {border-top: none;}
  .table, .blast-table {
      font-size:small;
      margin-bottom: 0px;
  }
  .table td, .table th {
    border-top: none;
    vertical-align: middle;
  }
  .blast-table thead tr th {
    border-bottom-width: 1px;
  }
  .blast-table tbody tr td {
    border: none;
  }
  .list-group {
      margin-top: 5vh;
      height: 85vh;
      overflow-y:auto; 
  }
  .listgroupitem {
      cursor:pointer;
  }
  .listgroupitem:hover, .listgroupitem.active {
      cursor:pointer;
      background-color: #dee2e663;
  }
  .tab-pane.active { animation-name: fadeIn; animation-duration: 300ms; animation-timing-function: linear; }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
  .scaffold-name{
      border-bottom: 2px solid #dee2e6;
  }
  .tab-pane {
      position: absolute;        
      height:100vh;
      width:inherit;
      z-index: 10;
  }
  .tab-pane #phage-1{
      z-index: 20;
  }
  .arrow { 
      z-index: -10;
      width: 1.25rem; 
      height: 1.25rem; 
      display: block; 
      position: relative; 
      margin: auto; 
  } 
  .arrow span { 
      top: 0.5rem; 
      position: absolute; 
      width: 0.75rem; 
      height: 0.1rem; 
      background-color: #495057d4; 
      display: inline-block; 
      transition: all 0.2s ease; 
  } 
  .arrow span:first-of-type { 
      left: 0; 
      -webkit-transform: rotate(45deg); 
      transform: rotate(45deg); 
  } 
  .arrow span:last-of-type { 
      right: 0; 
      -webkit-transform: rotate(-45deg); 
      transform: rotate(-45deg); 
  } 
  .arrow.active span:first-of-type { 
      -webkit-transform: rotate(-45deg); 
      transform: rotate(-45deg); 
  } 
  .arrow.active span:last-of-type { 
      -webkit-transform: rotate(45deg); 
      transform: rotate(45deg); 
  }
  .sk-fading-circle {
    margin: auto;
    margin-bottom: -0.3rem;
    margin-left: 3px;
    width: 1.2rem;
    height: 1.2rem;
    position: relative;
  }

  .sk-fading-circle .sk-circle {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0;
    top: 0;
  }

  .sk-fading-circle .sk-circle:before {
    content: '';
    display: block;
    margin: 0 auto;
    width: 15%;
    height: 15%;
    background-color: #343a40b5;
    border-radius: 100%;
    -webkit-animation: sk-circleFadeDelay 1.2s infinite ease-in-out both;
            animation: sk-circleFadeDelay 1.2s infinite ease-in-out both;
  }
  .sk-fading-circle .sk-circle2 {
    -webkit-transform: rotate(30deg);
        -ms-transform: rotate(30deg);
            transform: rotate(30deg);
  }
  .sk-fading-circle .sk-circle3 {
    -webkit-transform: rotate(60deg);
        -ms-transform: rotate(60deg);
            transform: rotate(60deg);
  }
  .sk-fading-circle .sk-circle4 {
    -webkit-transform: rotate(90deg);
        -ms-transform: rotate(90deg);
            transform: rotate(90deg);
  }
  .sk-fading-circle .sk-circle5 {
    -webkit-transform: rotate(120deg);
        -ms-transform: rotate(120deg);
            transform: rotate(120deg);
  }
  .sk-fading-circle .sk-circle6 {
    -webkit-transform: rotate(150deg);
        -ms-transform: rotate(150deg);
            transform: rotate(150deg);
  }
  .sk-fading-circle .sk-circle7 {
    -webkit-transform: rotate(180deg);
        -ms-transform: rotate(180deg);
            transform: rotate(180deg);
  }
  .sk-fading-circle .sk-circle8 {
    -webkit-transform: rotate(210deg);
        -ms-transform: rotate(210deg);
            transform: rotate(210deg);
  }
  .sk-fading-circle .sk-circle9 {
    -webkit-transform: rotate(240deg);
        -ms-transform: rotate(240deg);
            transform: rotate(240deg);
  }
  .sk-fading-circle .sk-circle10 {
    -webkit-transform: rotate(270deg);
        -ms-transform: rotate(270deg);
            transform: rotate(270deg);
  }
  .sk-fading-circle .sk-circle11 {
    -webkit-transform: rotate(300deg);
        -ms-transform: rotate(300deg);
            transform: rotate(300deg);
  }
  .sk-fading-circle .sk-circle12 {
    -webkit-transform: rotate(330deg);
        -ms-transform: rotate(330deg);
            transform: rotate(330deg);
  }
  .sk-fading-circle .sk-circle2:before {
    -webkit-animation-delay: -1.1s;
            animation-delay: -1.1s;
  }
  .sk-fading-circle .sk-circle3:before {
    -webkit-animation-delay: -1s;
            animation-delay: -1s;
  }
  .sk-fading-circle .sk-circle4:before {
    -webkit-animation-delay: -0.9s;
            animation-delay: -0.9s;
  }
  .sk-fading-circle .sk-circle5:before {
    -webkit-animation-delay: -0.8s;
            animation-delay: -0.8s;
  }
  .sk-fading-circle .sk-circle6:before {
    -webkit-animation-delay: -0.7s;
            animation-delay: -0.7s;
  }
  .sk-fading-circle .sk-circle7:before {
    -webkit-animation-delay: -0.6s;
            animation-delay: -0.6s;
  }
  .sk-fading-circle .sk-circle8:before {
    -webkit-animation-delay: -0.5s;
            animation-delay: -0.5s;
  }
  .sk-fading-circle .sk-circle9:before {
    -webkit-animation-delay: -0.4s;
            animation-delay: -0.4s;
  }
  .sk-fading-circle .sk-circle10:before {
    -webkit-animation-delay: -0.3s;
            animation-delay: -0.3s;
  }
  .sk-fading-circle .sk-circle11:before {
    -webkit-animation-delay: -0.2s;
            animation-delay: -0.2s;
  }
  .sk-fading-circle .sk-circle12:before {
    -webkit-animation-delay: -0.1s;
            animation-delay: -0.1s;
  }

  @-webkit-keyframes sk-circleFadeDelay {
    0%, 39%, 100% { opacity: 0; }
    40% { opacity: 1; }
  }

  @keyframes sk-circleFadeDelay {
    0%, 39%, 100% { opacity: 0; }
    40% { opacity: 1; }
  }

  /* ready icon */
   .download-sequence svg, .to-blast svg, .td-to-blast svg, .to-blast-all svg, .download-sequence-all svg {
    width: 1.2rem;
    display: inline-block;
    margin: auto;
    margin-left: 3px;
  }
  .ready-icon .path {
    stroke-dasharray: 1000;
    stroke-dashoffset: 0;
    &.circle {
      -webkit-animation: dash .9s ease-in-out;
      animation: dash .9s ease-in-out;
    }
    &.check {
      stroke-dashoffset: -100;
      -webkit-animation: dash-check .9s .35s ease-in-out forwards;
      animation: dash-check .9s .35s ease-in-out forwards;
    }
  }
  th svg {
    width: 1.7rem;
    margin-left: -0.55rem;
  }
  @-webkit-keyframes dash {
    0% {
      stroke-dashoffset: 1000;
    }
    100% {
      stroke-dashoffset: 0;
    }
  }

  @keyframes dash {
    0% {
      stroke-dashoffset: 1000;
    }
    100% {
      stroke-dashoffset: 0;
    }
  }

  @-webkit-keyframes dash-check {
    0% {
      stroke-dashoffset: -100;
    }
    100% {
      stroke-dashoffset: 900;
    }
  }

  @keyframes dash-check {
    0% {
      stroke-dashoffset: -100;
    }
    100% {
      stroke-dashoffset: 900;
    }
  }
  .to-blast, .td-to-blast, .download-sequence, .to-blast-all, .download-sequence-all {
    display: inline-block;
  }
  .download-sequence-all, .to-blast-all {
    cursor: pointer;
  }
  .download-sequence {
    float: right;
    padding-right:.3rem;
    cursor: pointer;
  }
  .to-blast:hover, .to-blast-click:hover {
    cursor:pointer;
  }
  .panel {
    margin-bottom: 20px;
    background-color: #fff;
    border: 1px solid #cacacade;
    border-radius: 4px;
    -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
    display: inline-block;
  }
  .panel-body {
    padding: 10px;
  }
  .panel-heading {
    padding: 7px 10px;
    border-bottom: 1px solid #cacacade;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    background-color: #dee2e663;
  }
  .panel-heading h6 {
        margin-bottom: 0px;
  }
  .panel-heading > .dropdown .dropdown-toggle {
    color: inherit;
  }
  .panel-title {
    margin-top: 0;
    margin-bottom: 0;
    font-size: 16px;
    color: inherit;
  }

  .accordeon-blast-panel.collapsing {
      transition: none;
  }
  .accordeon-blast-panel.show {
      animation-name: fadeIn; animation-duration: 300ms; animation-timing-function: linear;
  }
  .accordeon-blast-panel {
    padding-top:0 !important;
    padding-bottom: 0 !important;
  }
  .accordeon-blast-panel .panel{
    margin-top: 5px;
    margin-bottom: 5px;
  }
  .popover{ 
	max-width:30vw; 
	font-size: x-small; 
  } 
  @media(min-width: 992px) { 
     .popover{ 
	max-width:10vw; 
     } 
 }
ol {    padding-left: 0.75rem;
	margin-bottom:0;}
.panel{
      font-size: smaller;
    }
  div[data-toggle='popover']{
    display: inline-block;
  }
.blinking{
  color: #000;
	animation:blinkingText 1.8s infinite;
}
@keyframes blinkingText{
	0%{		opacity: 1.0;	}
	10%{opacity: 0.88;}
	20%{opacity: 0.76;}
	30%{	opacity: 0.64;	}
	40%{opacity: 0.52;}
	50%{	opacity: 0.40;	}
	60%{opacity:0.52;}
	70%{	opacity: 0.64;	}
	80%{opacity:0.76}
	90%{opacity:0.88}
	100%{	opacity: 1.0;	}
}
.accordeon-row {
	display:none;
}
.accordeon-row.show {
	display:table-row;
}
  </style>
  </head>
  '''

body_main = '''<body>
  <div class="container">
  <div class="row">
  {0}
  {1}
  </div>
  </div>
'''

body_table = '''<div class="col-md-12 col-lg-4 col-xl-4">
  <div class="list-group" id="list-tab" role="tablist">
  <table class="table">
  <thead>
  <tr>
  <th scope="col">#</th>
  <th scope="col">Coordinates</th>
  <th scope="col">Taxonomy</th>
  <th scope="col" style="text-align: center;">pVOGs</th>
  </tr>
  </thead>
  {0}
  </table>
  </div>
    <div class="do-for-all"> 
<div data-content="Click to Blast All" data-placement="right" data-toggle="popover" data-trigger="hover">
<small>For all prophage sequences:</small>
<div class="to-blast-all">
<svg viewbox="0 0 512 512.00076" width="512pt" xmlns="http://www.w3.org/2000/svg">
<path d="m509.070312 138.953125c-3.902343-3.90625-10.234374-3.90625-14.140624 0-1.367188 1.367187-2.765626 2.65625-4.191407 3.890625l-76.457031-76.460938c-3.902344-3.902343-10.234375-3.902343-14.140625 0-3.90625 3.90625-3.90625 10.238282 0 14.144532l73.550781 73.550781c-32.914062 15.960937-76.007812 9.238281-121.210937 1.9375-3.183594-18.378906-6.003907-36.34375-6.859375-53.460937l41.578125 41.578124c1.953125 1.953126 4.511719 2.929688 7.070312 2.929688 2.5625 0 5.121094-.980469 7.074219-2.929688 3.902344-3.90625 3.902344-10.238281 0-14.144531l-55.058594-55.054687c2.4375-21.535156 10.011719-41.113282 26.597656-57.695313l.175782-.175781c3.898437-3.914062 3.890625-10.242188-.019532-14.144531-3.914062-3.898438-10.246093-3.890625-14.144531.019531l-.167969.167969c-41.109374 41.109375-36.199218 95.464843-27.101562 149.601562-55.082031-8.386719-110.136719-12.363281-150.621094 28.121094-41.941406 41.941406-34.816406 98.542969-25.144531 154.3125-56.132813-8.96875-113.175781-15.988281-152.929687 23.765625-3.90625 3.90625-3.90625 10.238281 0 14.144531 1.953124 1.953125 4.511718 2.929688 7.070312 2.929688s5.117188-.980469 7.070312-2.929688c16.332032-16.335937 36.851563-23.007812 59.902344-24.546875l61.980469 61.980469c1.953125 1.953125 4.511719 2.929687 7.070313 2.929687 2.558593 0 5.117187-.976562 7.070312-2.929687 3.90625-3.90625 3.90625-10.238281 0-14.144531l-47.515625-47.515625c17.257813 1.277343 35.421875 4.167969 53.9375 7.160156 7.582031 43.71875 13.089844 85.089844-5.011719 118.3125l-83.433594-83.4375c-3.902343-3.902344-10.234374-3.902344-14.140624 0-3.90625 3.90625-3.90625 10.238281 0 14.144531l85.867187 85.867188c-1.175781 1.3125-2.398437 2.613281-3.679687 3.894531l-.175782.175781c-3.898437 3.910156-3.890625 10.242188.019532 14.140625 1.953124 1.945313 4.507812 2.917969 7.0625 2.917969 2.5625 0 5.128906-.980469 7.082031-2.9375l.164062-.167969c41.113281-41.109375 36.199219-95.464843 27.105469-149.601562 55.082031 8.386719 110.136719 12.363281 150.621094-28.121094 41.941406-41.941406 34.8125-98.542969 25.144531-154.308594 56.132813 8.964844 113.175781 15.988281 152.929687-23.765625 3.90625-3.90625 3.90625-10.238281 0-14.144531zm-173.820312 34.554687c4.257812 24.203126 8.242188 47.777344 8.308594 69.691407l-36.722656-36.71875c-3.90625-3.90625-10.234376-3.90625-14.144532 0-3.902344 3.902343-3.902344 10.234375 0 14.140625l48.699219 48.699218c-2.703125 14.578126-8.191406 28.082032-17.785156 40.144532l-121.097657-121.101563c34.777344-27.957031 82.148438-22.839843 132.742188-14.855469zm-158.496094 164.988282c-4.269531-24.238282-8.257812-47.847656-8.3125-69.789063l37.425782 37.425781c1.953124 1.953126 4.511718 2.929688 7.070312 2.929688 2.5625 0 5.121094-.976562 7.074219-2.929688 3.902343-3.90625 3.902343-10.238281 0-14.140624l-49.386719-49.386719c2.707031-14.546875 8.191406-28.03125 17.769531-40.070313l121.101563 121.105469c-34.777344 27.953125-82.152344 22.839844-132.742188 14.855469zm0 0"></path><path d="m243.515625 315.492188-.097656-.09375c-3.90625-3.90625-10.234375-3.90625-14.140625 0-3.90625 3.902343-3.90625 10.234374 0 14.140624l.09375.09375c1.953125 1.953126 4.511718 2.929688 7.070312 2.929688s5.117188-.976562 7.070313-2.929688c3.90625-3.902343 3.90625-10.234374.003906-14.140624zm0 0"></path><path d="m269.191406 197.121094.097656.09375c1.953126 1.953125 4.511719 2.929687 7.070313 2.929687s5.117187-.976562 7.070313-2.929687c3.90625-3.90625 3.90625-10.238282 0-14.144532l-.09375-.09375c-3.90625-3.90625-10.238282-3.90625-14.144532 0-3.902344 3.90625-3.902344 10.238282 0 14.144532zm0 0"></path>
</svg>
</div>
</div>
<div class="download-sequence-all" data-target="">
<div data-content="Click to download all prophage sequences in fasta-format." data-placement="right" data-toggle="popover" data-trigger="hover">
<svg id="Capa_1" style="enable-background:new 0 0 41.712 41.712;" version="1.1" viewbox="0 0 41.712 41.712" x="0px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" y="0px">
<path d="M31.586,21.8c0.444-0.444,0.444-1.143,0-1.587c-0.429-0.444-1.143-0.444-1.571,0l-8.047,8.032V1.706
                                      c0-0.619-0.492-1.127-1.111-1.127c-0.619,0-1.127,0.508-1.127,1.127v26.539l-8.031-8.032c-0.444-0.444-1.159-0.444-1.587,0
                                      c-0.444,0.444-0.444,1.143,0,1.587l9.952,9.952c0.429,0.429,1.143,0.429,1.587,0L31.586,21.8z M39.474,29.086
                                      c0-0.619,0.492-1.111,1.111-1.111c0.619,0,1.127,0.492,1.127,1.111v10.92c0,0.619-0.508,1.127-1.127,1.127H1.111
                                      C0.492,41.133,0,40.625,0,40.006v-10.92c0-0.619,0.492-1.111,1.111-1.111s1.127,0.492,1.127,1.111v9.809h37.236V29.086z" style="fill:#1E201D;"></path>
</svg>
</div>
</div>
  </div>
  </div>
'''

body_plots = '''<div class="col-md-12 col-lg-8 col-xl-8 tab-content" id="nav-tabContent">{0}</div>'''

transposable_index = '''<div data-toggle="popover" data-trigger="hover" data-placement="right" data-content="This prophage may contain transposable elements.">
<svg version="1.1" class="transpose" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
   viewBox="0 0 490.1 490.1" style="enable-background:new 0 0 490.1 490.1;" xml:space="preserve">
<g>
    <path d="m386.9,12.2l-281.6,0c-28.2,0 -51.1,19.229653 -51.1,42.909836l0,195.739391l-32.3,-27.123047c-4.8,-4.03067 -12.5,-4.03067 -17.3,0s-4.8,10.496535 0,14.527205l53.3,44.757227c2.4,2.015335 5.5,3.023002 8.7,3.023002s6.3,-1.007667 8.7,-3.023002l53.3,-44.757227c4.8,-4.03067 4.8,-10.496535 0,-14.527205c-4.8,-4.03067 -12.5,-4.03067 -17.3,0l-32.4,27.20702l0,-195.823363c0,-12.343926 11.9,-22.336627 26.6,-22.336627l281.5,0c14.7,0 26.6,9.992702 26.6,22.336627l0,28.550576c0,5.710115 5.5,10.328591 12.3,10.328591s12.3,-4.618476 12.3,-10.328591l0,-28.550576c-0.3,-23.596211 -23.2,-42.909836 -51.3,-42.909836z"/>
    <path d="m417,129.17339l-53.3,44.757227c-4.8,4.03067 -4.8,10.496535 0,14.527205c2.4,2.015335 5.5,3.023002 8.7,3.023002s6.3,-1.007667 8.7,-3.023002l32.4,-27.20702l0,195.739391c0,12.343926 -11.9,22.336627 -26.6,22.336627l-281.6,0c-14.7,0 -26.6,-9.992702 -26.6,-22.336627l0,-28.550576c0,-5.710115 -5.5,-10.328591 -12.3,-10.328591s-12.3,4.618476 -12.3,10.328591l0,28.550576c0,23.680184 22.9,42.909836 51.1,42.909836l281.5,0c28.2,0 51.1,-19.229653 51.1,-42.909836l0,-195.739391l32.4,27.20702c4.8,4.03067 12.5,4.03067 17.3,0s4.8,-10.496535 0,-14.527205l-53.3,-44.757227c-4.4,-3.862725 -12.6,-3.862725 -17.2,0z"/>
 </g>
<text x="250" y="300" fill='black' font-size="220"  text-anchor="middle" alignment-baseline="baseline">{0}</text>
</svg>
</div>
'''

row = '''<tr class="ListGroupItem {6}" data-href="phage-{0}" id="tab-phage-{0}">
    <th scope="row">{7}</th>
    <td>{1} - {2}
        <div id='blast-phage-{0}' class="to-blast">
            <div id='accordeon-blast-{0}-id' class="accordion-toggle" data-target="#accordeon-blast-{0}" data-toggle="collapse">
                <div data-toggle="popover" data-target="#general-blast-info" data-trigger="hover" data-placement="right" data-content="Click to see blast options. Your blast links will be saved here until they are available.">
                    <svg viewBox="0 0 512 512.00076" width="512pt" xmlns="http://www.w3.org/2000/svg">
                        <path d="m509.070312 138.953125c-3.902343-3.90625-10.234374-3.90625-14.140624 0-1.367188 1.367187-2.765626 2.65625-4.191407 3.890625l-76.457031-76.460938c-3.902344-3.902343-10.234375-3.902343-14.140625 0-3.90625 3.90625-3.90625 10.238282 0 14.144532l73.550781 73.550781c-32.914062 15.960937-76.007812 9.238281-121.210937 1.9375-3.183594-18.378906-6.003907-36.34375-6.859375-53.460937l41.578125 41.578124c1.953125 1.953126 4.511719 2.929688 7.070312 2.929688 2.5625 0 5.121094-.980469 7.074219-2.929688 3.902344-3.90625 3.902344-10.238281 0-14.144531l-55.058594-55.054687c2.4375-21.535156 10.011719-41.113282 26.597656-57.695313l.175782-.175781c3.898437-3.914062 3.890625-10.242188-.019532-14.144531-3.914062-3.898438-10.246093-3.890625-14.144531.019531l-.167969.167969c-41.109374 41.109375-36.199218 95.464843-27.101562 149.601562-55.082031-8.386719-110.136719-12.363281-150.621094 28.121094-41.941406 41.941406-34.816406 98.542969-25.144531 154.3125-56.132813-8.96875-113.175781-15.988281-152.929687 23.765625-3.90625 3.90625-3.90625 10.238281 0 14.144531 1.953124 1.953125 4.511718 2.929688 7.070312 2.929688s5.117188-.980469 7.070312-2.929688c16.332032-16.335937 36.851563-23.007812 59.902344-24.546875l61.980469 61.980469c1.953125 1.953125 4.511719 2.929687 7.070313 2.929687 2.558593 0 5.117187-.976562 7.070312-2.929687 3.90625-3.90625 3.90625-10.238281 0-14.144531l-47.515625-47.515625c17.257813 1.277343 35.421875 4.167969 53.9375 7.160156 7.582031 43.71875 13.089844 85.089844-5.011719 118.3125l-83.433594-83.4375c-3.902343-3.902344-10.234374-3.902344-14.140624 0-3.90625 3.90625-3.90625 10.238281 0 14.144531l85.867187 85.867188c-1.175781 1.3125-2.398437 2.613281-3.679687 3.894531l-.175782.175781c-3.898437 3.910156-3.890625 10.242188.019532 14.140625 1.953124 1.945313 4.507812 2.917969 7.0625 2.917969 2.5625 0 5.128906-.980469 7.082031-2.9375l.164062-.167969c41.113281-41.109375 36.199219-95.464843 27.105469-149.601562 55.082031 8.386719 110.136719 12.363281 150.621094-28.121094 41.941406-41.941406 34.8125-98.542969 25.144531-154.308594 56.132813 8.964844 113.175781 15.988281 152.929687-23.765625 3.90625-3.90625 3.90625-10.238281 0-14.144531zm-173.820312 34.554687c4.257812 24.203126 8.242188 47.777344 8.308594 69.691407l-36.722656-36.71875c-3.90625-3.90625-10.234376-3.90625-14.144532 0-3.902344 3.902343-3.902344 10.234375 0 14.140625l48.699219 48.699218c-2.703125 14.578126-8.191406 28.082032-17.785156 40.144532l-121.097657-121.101563c34.777344-27.957031 82.148438-22.839843 132.742188-14.855469zm-158.496094 164.988282c-4.269531-24.238282-8.257812-47.847656-8.3125-69.789063l37.425782 37.425781c1.953124 1.953126 4.511718 2.929688 7.070312 2.929688 2.5625 0 5.121094-.976562 7.074219-2.929688 3.902343-3.90625 3.902343-10.238281 0-14.140624l-49.386719-49.386719c2.707031-14.546875 8.191406-28.03125 17.769531-40.070313l121.101563 121.105469c-34.777344 27.953125-82.152344 22.839844-132.742188 14.855469zm0 0"/><path d="m243.515625 315.492188-.097656-.09375c-3.90625-3.90625-10.234375-3.90625-14.140625 0-3.90625 3.902343-3.90625 10.234374 0 14.140624l.09375.09375c1.953125 1.953126 4.511718 2.929688 7.070312 2.929688s5.117188-.976562 7.070313-2.929688c3.90625-3.902343 3.90625-10.234374.003906-14.140624zm0 0"/><path d="m269.191406 197.121094.097656.09375c1.953126 1.953125 4.511719 2.929687 7.070313 2.929687s5.117187-.976562 7.070313-2.929687c3.90625-3.90625 3.90625-10.238282 0-14.144532l-.09375-.09375c-3.90625-3.90625-10.238282-3.90625-14.144532 0-3.902344 3.90625-3.902344 10.238282 0 14.144532zm0 0"/>
                    </svg>
                </div>
            </div>
        </div>
    </td>
    <td>{3}</td>
    <td id='accordeon-phage-{0}-id' class="accordion-toggle" data-target="#accordeon-phage-{0}" data-toggle="collapse">
        <a class="arrow"><span></span><span></span></a>
    </td>
<tr class="accordeon-row">
    <td class="td-collapse collapse accordeon-blast-panel" colspan="4" id="td-accordeon-blast-{0}">
        <div class="accordion-body collapse accordeon-blast-panel" id="accordeon-blast-{0}" sequence="{4}">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h6>Databases to Blast Against
                        <div class="download-sequence" data-target="#accordeon-blast-{0}">
                            <div data-toggle="popover" data-trigger="hover" data-placement="right" data-content="Click to download prophage sequence in fasta-format.">
                                <svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 41.712 41.712" style="enable-background:new 0 0 41.712 41.712;" xml:space="preserve">
                                    <path style="fill:#1E201D;" d="M31.586,21.8c0.444-0.444,0.444-1.143,0-1.587c-0.429-0.444-1.143-0.444-1.571,0l-8.047,8.032V1.706
                                      c0-0.619-0.492-1.127-1.111-1.127c-0.619,0-1.127,0.508-1.127,1.127v26.539l-8.031-8.032c-0.444-0.444-1.159-0.444-1.587,0
                                      c-0.444,0.444-0.444,1.143,0,1.587l9.952,9.952c0.429,0.429,1.143,0.429,1.587,0L31.586,21.8z M39.474,29.086
                                      c0-0.619,0.492-1.111,1.111-1.111c0.619,0,1.127,0.492,1.127,1.111v10.92c0,0.619-0.508,1.127-1.127,1.127H1.111
                                      C0.492,41.133,0,40.625,0,40.006v-10.92c0-0.619,0.492-1.111,1.111-1.111s1.127,0.492,1.127,1.111v9.809h37.236V29.086z"/>
                              </svg>
                            </div>
                        </div>
                    </h6>
                </div>
                <div class="panel-body">
                    <table class="blast-table table-sm">
                        <tbody>
                        <tr>
                            <td> Nucleotide collection (nr/nt) </td>
                            <td id="blast-{0}-nt" class="td-to-blast">
                                <div data-toggle="popover" data-target="#general-blast-info" data-trigger="hover" data-placement="right" data-content="Click to Blast.">
                                    <div class="to-blast-click" data-target="blast-{0}-nt" db="nt">
                                        <svg viewBox="0 0 512 512.00076" width="512pt" xmlns="http://www.w3.org/2000/svg">
                                            <path d="m509.070312 138.953125c-3.902343-3.90625-10.234374-3.90625-14.140624 0-1.367188 1.367187-2.765626 2.65625-4.191407 3.890625l-76.457031-76.460938c-3.902344-3.902343-10.234375-3.902343-14.140625 0-3.90625 3.90625-3.90625 10.238282 0 14.144532l73.550781 73.550781c-32.914062 15.960937-76.007812 9.238281-121.210937 1.9375-3.183594-18.378906-6.003907-36.34375-6.859375-53.460937l41.578125 41.578124c1.953125 1.953126 4.511719 2.929688 7.070312 2.929688 2.5625 0 5.121094-.980469 7.074219-2.929688 3.902344-3.90625 3.902344-10.238281 0-14.144531l-55.058594-55.054687c2.4375-21.535156 10.011719-41.113282 26.597656-57.695313l.175782-.175781c3.898437-3.914062 3.890625-10.242188-.019532-14.144531-3.914062-3.898438-10.246093-3.890625-14.144531.019531l-.167969.167969c-41.109374 41.109375-36.199218 95.464843-27.101562 149.601562-55.082031-8.386719-110.136719-12.363281-150.621094 28.121094-41.941406 41.941406-34.816406 98.542969-25.144531 154.3125-56.132813-8.96875-113.175781-15.988281-152.929687 23.765625-3.90625 3.90625-3.90625 10.238281 0 14.144531 1.953124 1.953125 4.511718 2.929688 7.070312 2.929688s5.117188-.980469 7.070312-2.929688c16.332032-16.335937 36.851563-23.007812 59.902344-24.546875l61.980469 61.980469c1.953125 1.953125 4.511719 2.929687 7.070313 2.929687 2.558593 0 5.117187-.976562 7.070312-2.929687 3.90625-3.90625 3.90625-10.238281 0-14.144531l-47.515625-47.515625c17.257813 1.277343 35.421875 4.167969 53.9375 7.160156 7.582031 43.71875 13.089844 85.089844-5.011719 118.3125l-83.433594-83.4375c-3.902343-3.902344-10.234374-3.902344-14.140624 0-3.90625 3.90625-3.90625 10.238281 0 14.144531l85.867187 85.867188c-1.175781 1.3125-2.398437 2.613281-3.679687 3.894531l-.175782.175781c-3.898437 3.910156-3.890625 10.242188.019532 14.140625 1.953124 1.945313 4.507812 2.917969 7.0625 2.917969 2.5625 0 5.128906-.980469 7.082031-2.9375l.164062-.167969c41.113281-41.109375 36.199219-95.464843 27.105469-149.601562 55.082031 8.386719 110.136719 12.363281 150.621094-28.121094 41.941406-41.941406 34.8125-98.542969 25.144531-154.308594 56.132813 8.964844 113.175781 15.988281 152.929687-23.765625 3.90625-3.90625 3.90625-10.238281 0-14.144531zm-173.820312 34.554687c4.257812 24.203126 8.242188 47.777344 8.308594 69.691407l-36.722656-36.71875c-3.90625-3.90625-10.234376-3.90625-14.144532 0-3.902344 3.902343-3.902344 10.234375 0 14.140625l48.699219 48.699218c-2.703125 14.578126-8.191406 28.082032-17.785156 40.144532l-121.097657-121.101563c34.777344-27.957031 82.148438-22.839843 132.742188-14.855469zm-158.496094 164.988282c-4.269531-24.238282-8.257812-47.847656-8.3125-69.789063l37.425782 37.425781c1.953124 1.953126 4.511718 2.929688 7.070312 2.929688 2.5625 0 5.121094-.976562 7.074219-2.929688 3.902343-3.90625 3.902343-10.238281 0-14.140624l-49.386719-49.386719c2.707031-14.546875 8.191406-28.03125 17.769531-40.070313l121.101563 121.105469c-34.777344 27.953125-82.152344 22.839844-132.742188 14.855469zm0 0"/><path d="m243.515625 315.492188-.097656-.09375c-3.90625-3.90625-10.234375-3.90625-14.140625 0-3.90625 3.902343-3.90625 10.234374 0 14.140624l.09375.09375c1.953125 1.953126 4.511718 2.929688 7.070312 2.929688s5.117188-.976562 7.070313-2.929688c3.90625-3.902343 3.90625-10.234374.003906-14.140624zm0 0"/><path d="m269.191406 197.121094.097656.09375c1.953126 1.953125 4.511719 2.929687 7.070313 2.929687s5.117187-.976562 7.070313-2.929687c3.90625-3.90625 3.90625-10.238282 0-14.144532l-.09375-.09375c-3.90625-3.90625-10.238282-3.90625-14.144532 0-3.902344 3.90625-3.902344 10.238282 0 14.144532zm0 0"/>
                                        </svg>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>RefSeq Genome Database (refseq_genomes)</td>
                            <td id="blast-{0}-refseq" class="td-to-blast">
                                <div data-toggle="popover" data-target="#general-blast-info" data-trigger="hover" data-placement="right" data-content="Click to Blast.">
                                    <div class="to-blast-click" data-target="blast-{0}-refseq" db="refseq_genomes&EQ_MENU=Bacteria%20(taxid:2)">
                                        <svg viewBox="0 0 512 512.00076" width="512pt" xmlns="http://www.w3.org/2000/svg">
                                            <path d="m509.070312 138.953125c-3.902343-3.90625-10.234374-3.90625-14.140624 0-1.367188 1.367187-2.765626 2.65625-4.191407 3.890625l-76.457031-76.460938c-3.902344-3.902343-10.234375-3.902343-14.140625 0-3.90625 3.90625-3.90625 10.238282 0 14.144532l73.550781 73.550781c-32.914062 15.960937-76.007812 9.238281-121.210937 1.9375-3.183594-18.378906-6.003907-36.34375-6.859375-53.460937l41.578125 41.578124c1.953125 1.953126 4.511719 2.929688 7.070312 2.929688 2.5625 0 5.121094-.980469 7.074219-2.929688 3.902344-3.90625 3.902344-10.238281 0-14.144531l-55.058594-55.054687c2.4375-21.535156 10.011719-41.113282 26.597656-57.695313l.175782-.175781c3.898437-3.914062 3.890625-10.242188-.019532-14.144531-3.914062-3.898438-10.246093-3.890625-14.144531.019531l-.167969.167969c-41.109374 41.109375-36.199218 95.464843-27.101562 149.601562-55.082031-8.386719-110.136719-12.363281-150.621094 28.121094-41.941406 41.941406-34.816406 98.542969-25.144531 154.3125-56.132813-8.96875-113.175781-15.988281-152.929687 23.765625-3.90625 3.90625-3.90625 10.238281 0 14.144531 1.953124 1.953125 4.511718 2.929688 7.070312 2.929688s5.117188-.980469 7.070312-2.929688c16.332032-16.335937 36.851563-23.007812 59.902344-24.546875l61.980469 61.980469c1.953125 1.953125 4.511719 2.929687 7.070313 2.929687 2.558593 0 5.117187-.976562 7.070312-2.929687 3.90625-3.90625 3.90625-10.238281 0-14.144531l-47.515625-47.515625c17.257813 1.277343 35.421875 4.167969 53.9375 7.160156 7.582031 43.71875 13.089844 85.089844-5.011719 118.3125l-83.433594-83.4375c-3.902343-3.902344-10.234374-3.902344-14.140624 0-3.90625 3.90625-3.90625 10.238281 0 14.144531l85.867187 85.867188c-1.175781 1.3125-2.398437 2.613281-3.679687 3.894531l-.175782.175781c-3.898437 3.910156-3.890625 10.242188.019532 14.140625 1.953124 1.945313 4.507812 2.917969 7.0625 2.917969 2.5625 0 5.128906-.980469 7.082031-2.9375l.164062-.167969c41.113281-41.109375 36.199219-95.464843 27.105469-149.601562 55.082031 8.386719 110.136719 12.363281 150.621094-28.121094 41.941406-41.941406 34.8125-98.542969 25.144531-154.308594 56.132813 8.964844 113.175781 15.988281 152.929687-23.765625 3.90625-3.90625 3.90625-10.238281 0-14.144531zm-173.820312 34.554687c4.257812 24.203126 8.242188 47.777344 8.308594 69.691407l-36.722656-36.71875c-3.90625-3.90625-10.234376-3.90625-14.144532 0-3.902344 3.902343-3.902344 10.234375 0 14.140625l48.699219 48.699218c-2.703125 14.578126-8.191406 28.082032-17.785156 40.144532l-121.097657-121.101563c34.777344-27.957031 82.148438-22.839843 132.742188-14.855469zm-158.496094 164.988282c-4.269531-24.238282-8.257812-47.847656-8.3125-69.789063l37.425782 37.425781c1.953124 1.953126 4.511718 2.929688 7.070312 2.929688 2.5625 0 5.121094-.976562 7.074219-2.929688 3.902343-3.90625 3.902343-10.238281 0-14.140624l-49.386719-49.386719c2.707031-14.546875 8.191406-28.03125 17.769531-40.070313l121.101563 121.105469c-34.777344 27.953125-82.152344 22.839844-132.742188 14.855469zm0 0"/><path d="m243.515625 315.492188-.097656-.09375c-3.90625-3.90625-10.234375-3.90625-14.140625 0-3.90625 3.902343-3.90625 10.234374 0 14.140624l.09375.09375c1.953125 1.953126 4.511718 2.929688 7.070312 2.929688s5.117188-.976562 7.070313-2.929688c3.90625-3.902343 3.90625-10.234374.003906-14.140624zm0 0"/><path d="m269.191406 197.121094.097656.09375c1.953126 1.953125 4.511719 2.929687 7.070313 2.929687s5.117187-.976562 7.070313-2.929687c3.90625-3.90625 3.90625-10.238282 0-14.144532l-.09375-.09375c-3.90625-3.90625-10.238282-3.90625-14.144532 0-3.902344 3.90625-3.902344 10.238282 0 14.144532zm0 0"/>
                                        </svg>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </td>
</tr>
<tr class="accordeon-row">
    <td class="td-collapse collapse" colspan="4" id="td-accordeon-phage-{0}">
        <div class="accordion-body collapse" id="accordeon-phage-{0}">{5}
        </div>
    </td>
</tr>
</tr>
'''

footer = '''<script type="text/javascript">
    var blast_loading_icon = '<div data-toggle="popover" data-trigger="hover" data-placement="right" data-content="Click to follow the process by yourself."><div class="class-sk-fading-circle sk-fading-circle blast-icons">  <div class="sk-circle1 sk-circle"></div>  <div class="sk-circle2 sk-circle"></div>  <div class="sk-circle3 sk-circle"></div>  <div class="sk-circle4 sk-circle"></div>  <div class="sk-circle5 sk-circle"></div>  <div class="sk-circle6 sk-circle"></div>  <div class="sk-circle7 sk-circle"></div>  <div class="sk-circle8 sk-circle"></div>  <div class="sk-circle9 sk-circle"></div>  <div class="sk-circle10 sk-circle"></div>  <div class="sk-circle11 sk-circle"></div>  <div class="sk-circle12 sk-circle"></div></div></div>';
    var blast_ready_icon = '<div data-toggle="popover" data-trigger="hover" data-placement="right" data-content="Click to see the results!"><div class="blast-icons ready-icon">	<svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 130.2 130.2">  <circle class="path circle" fill="none" stroke="#73AF55" stroke-width="6" stroke-miterlimit="10" cx="65.1" cy="65.1" r="62.1"/>  <polyline class="path check" fill="none" stroke="#73AF55" stroke-width="6" stroke-linecap="round" stroke-miterlimit="10" points="100.2,40.2 51.5,88.8 29.8,67.5 "/></svg></div></div>';
    var blast_stopwatch_icon = '<div data-toggle="popover" data-trigger="hover" data-placement="right" data-content="The time of waiting for results is up. You can reload the page or click  to follow the process by yourself."><div class="stopwatch-icon blast-icons">	<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"	 viewBox="0 0 60.001 60.001" style="enable-background:new 0 0 60.001 60.001;" xml:space="preserve"><g style="fill:#E84849;">	<path d="M59.693,56.636L47.849,36.33c-0.405-0.695-1.128-1.11-1.934-1.11c-0.805,0-1.527,0.415-1.933,1.11L32.137,56.636		c-0.409,0.7-0.412,1.539-0.008,2.242c0.404,0.703,1.129,1.123,1.94,1.123h23.691c0.811,0,1.536-0.42,1.939-1.123		C60.104,58.175,60.102,57.337,59.693,56.636z M57.966,57.882c-0.03,0.055-0.092,0.119-0.205,0.119H34.07		c-0.114,0-0.175-0.064-0.206-0.119s-0.056-0.14,0.001-0.238L45.71,37.338c0.057-0.098,0.143-0.118,0.205-0.118		c0.063,0,0.148,0.021,0.206,0.118l11.845,20.306C58.022,57.742,57.998,57.827,57.966,57.882z"/>	<path d="M46,42.001c-0.552,0-1,0.447-1,1v8c0,0.553,0.448,1,1,1s1-0.447,1-1v-8C47,42.448,46.552,42.001,46,42.001z"/>	<path d="M45.3,54.291c-0.19,0.18-0.3,0.439-0.3,0.71c0,0.26,0.11,0.52,0.29,0.71c0.19,0.18,0.45,0.29,0.71,0.29		c0.26,0,0.52-0.11,0.71-0.29c0.18-0.19,0.29-0.45,0.29-0.71c0-0.271-0.11-0.53-0.29-0.71C46.33,53.921,45.66,53.921,45.3,54.291z"		/>	<path d="M34,29.88c0-1.859-1.28-3.411-3-3.858V15.88c0-0.553-0.448-1-1-1s-1,0.447-1,1v10.142		c-1.399,0.364-2.494,1.459-2.858,2.858H19c-0.552,0-1,0.447-1,1s0.448,1,1,1h7.142c0.447,1.721,2,3,3.858,3		C32.206,33.88,34,32.086,34,29.88z M30,31.88c-1.103,0-2-0.897-2-2s0.897-2,2-2s2,0.897,2,2S31.103,31.88,30,31.88z"/>	<path d="M29,7.88v1c0,0.553,0.448,1,1,1s1-0.447,1-1v-1c0-0.553-0.448-1-1-1S29,7.327,29,7.88z"/>	<path d="M51,28.88c-0.553,0-1,0.447-1,1s0.447,1,1,1h1c0.553,0,1-0.447,1-1s-0.447-1-1-1H51z"/>	<path d="M8,28.88c-0.552,0-1,0.447-1,1s0.448,1,1,1h1c0.552,0,1-0.447,1-1s-0.448-1-1-1H8z"/>	<path d="M44.849,13.616l-0.707,0.707c-0.391,0.391-0.391,1.023,0,1.414c0.195,0.195,0.451,0.293,0.707,0.293		s0.512-0.098,0.707-0.293l0.707-0.707c0.391-0.391,0.391-1.023,0-1.414S45.24,13.225,44.849,13.616z"/>	<path d="M14.444,44.021l-0.707,0.707c-0.391,0.391-0.391,1.023,0,1.414c0.195,0.195,0.451,0.293,0.707,0.293		s0.512-0.098,0.707-0.293l0.707-0.707c0.391-0.391,0.391-1.023,0-1.414S14.834,43.631,14.444,44.021z"/>	<path d="M15.858,14.323l-0.707-0.707c-0.391-0.391-1.023-0.391-1.414,0s-0.391,1.023,0,1.414l0.707,0.707		c0.195,0.195,0.451,0.293,0.707,0.293s0.512-0.098,0.707-0.293C16.249,15.346,16.249,14.714,15.858,14.323z"/>	<path d="M23.243,57.18C10.735,54.082,2,42.905,2,30.001c0-15.439,12.561-28,28-28s28,12.561,28,28		c0,3.468-0.634,6.863-1.883,10.094c-0.199,0.515,0.057,1.094,0.572,1.293c0.512,0.199,1.094-0.058,1.293-0.572		C59.321,37.354,60,33.716,60,30.001c0-16.542-13.458-30-30-30s-30,13.458-30,30c0,13.825,9.36,25.801,22.762,29.121		c0.081,0.02,0.162,0.029,0.242,0.029c0.449,0,0.857-0.305,0.97-0.76C24.106,57.855,23.779,57.313,23.243,57.18z"/></g></svg></div>';
    var blast_warning_icon = '<div data-toggle="popover" data-trigger="hover" data-placement="right" data-content="No hits were found. Click to see the report."><div class="warning-icon blast-icons">	<svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"	 viewBox="0 0 508.52 508.52" style="enable-background:new 0 0 508.52 508.52;" xml:space="preserve"><g style="fill:#E84849;">	<path d="M254.26,0C113.845,0,0,113.845,0,254.26s113.845,254.26,254.26,254.26		s254.26-113.845,254.26-254.26S394.675,0,254.26,0z M254.26,476.737c-122.68,0-222.477-99.829-222.477-222.477		c0-122.68,99.797-222.477,222.477-222.477c122.649,0,222.477,99.797,222.477,222.477		C476.737,376.908,376.908,476.737,254.26,476.737z"/>	<path  d="M254.26,95.347c-17.544,0-31.782,14.239-31.782,31.782v158.912		c0,17.544,14.239,31.782,31.782,31.782s31.782-14.239,31.782-31.782V127.13C286.042,109.586,271.804,95.347,254.26,95.347z"/>	<circle  cx="254.26" cy="380.881" r="31.782"/></g></svg></div></div>';
    var blast_problem_icon = '<div data-toggle="popover" data-trigger="hover" data-placement="right" data-content="Some problems occurred with your sequence. Click to see the report or reload the page and try to blast again."><div class="blast-problem-icon blast-icons">	<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"	 viewBox="0 0 473.931 473.931" style="enable-background:new 0 0 473.931 473.931;" xml:space="preserve"><circle style="fill:#E84849;" cx="236.966" cy="236.966" r="236.966"/><path style="fill:#F4F5F5;" d="M429.595,245.83c0,16.797-13.624,30.417-30.417,30.417H74.73c-16.797,0-30.421-13.62-30.421-30.417	v-17.743c0-16.797,13.624-30.417,30.421-30.417h324.448c16.793,0,30.417,13.62,30.417,30.417V245.83z"/></svg></div></div>';
    var blast_fail_icon_for_check = '<div data-toggle="popover" data-trigger="hover" data-placement="right" data-content="Cannot get the response from Blast. Please, check your Internet connection and reload the page or click to follow the process manually. If you use Chrome, check if CORS extension is enabled."><div class="blast-fail-icon blast-icons"><svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 543.987 543.987" style="enable-background:new 0 0 543.987 543.987;" xml:space="preserve"><g ><path style="fill:#E84849;" d="M85.265,74.203C-23.952,177.311-28.901,349.431,74.207,458.647c1.811,1.925,3.655,3.818,5.526,5.684 c106.203,106.209,278.398,106.209,384.596,0c106.209-106.198,106.209-278.393,0-384.596C360.297-24.391,192.3-26.844,85.265,74.203 z M137.431,191.268l53.841-53.841l80.765,80.765l80.765-80.765l53.847,53.841l-80.765,80.792l80.77,80.737l-53.847,53.847 l-80.765-80.77l-80.765,80.77l-53.841-53.847l80.759-80.737L137.431,191.268z"/></svg></div></div>';
    var blast_fail_icon = '<div data-toggle="popover" data-trigger="hover" data-placement="right" data-content="Cannot get the response from Blast. Please, check your Internet connection and reload the page. If you use Chrome, check if CORS extension is enabled."><div class="blast-fail-icon blast-icons"><svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 543.987 543.987" style="enable-background:new 0 0 543.987 543.987;" xml:space="preserve"><g ><path style="fill:#E84849;" d="M85.265,74.203C-23.952,177.311-28.901,349.431,74.207,458.647c1.811,1.925,3.655,3.818,5.526,5.684 c106.203,106.209,278.398,106.209,384.596,0c106.209-106.198,106.209-278.393,0-384.596C360.297-24.391,192.3-26.844,85.265,74.203 z M137.431,191.268l53.841-53.841l80.765,80.765l80.765-80.765l53.847,53.841l-80.765,80.792l80.77,80.737l-53.847,53.847 l-80.765-80.77l-80.765,80.77l-53.841-53.847l80.759-80.737L137.431,191.268z"/></svg></div></div>';
    var blast_waiting_icon = '<div data-toggle="popover" data-trigger="manual" data-placement="right"><div class="blast-fail-icon blast-icons blinking"><svg viewbox="0 0 512 512.00076" width="512pt" xmlns="http://www.w3.org/2000/svg"><path d="m509.070312 138.953125c-3.902343-3.90625-10.234374-3.90625-14.140624 0-1.367188 1.367187-2.765626 2.65625-4.191407 3.890625l-76.457031-76.460938c-3.902344-3.902343-10.234375-3.902343-14.140625 0-3.90625 3.90625-3.90625 10.238282 0 14.144532l73.550781 73.550781c-32.914062 15.960937-76.007812 9.238281-121.210937 1.9375-3.183594-18.378906-6.003907-36.34375-6.859375-53.460937l41.578125 41.578124c1.953125 1.953126 4.511719 2.929688 7.070312 2.929688 2.5625 0 5.121094-.980469 7.074219-2.929688 3.902344-3.90625 3.902344-10.238281 0-14.144531l-55.058594-55.054687c2.4375-21.535156 10.011719-41.113282 26.597656-57.695313l.175782-.175781c3.898437-3.914062 3.890625-10.242188-.019532-14.144531-3.914062-3.898438-10.246093-3.890625-14.144531.019531l-.167969.167969c-41.109374 41.109375-36.199218 95.464843-27.101562 149.601562-55.082031-8.386719-110.136719-12.363281-150.621094 28.121094-41.941406 41.941406-34.816406 98.542969-25.144531 154.3125-56.132813-8.96875-113.175781-15.988281-152.929687 23.765625-3.90625 3.90625-3.90625 10.238281 0 14.144531 1.953124 1.953125 4.511718 2.929688 7.070312 2.929688s5.117188-.980469 7.070312-2.929688c16.332032-16.335937 36.851563-23.007812 59.902344-24.546875l61.980469 61.980469c1.953125 1.953125 4.511719 2.929687 7.070313 2.929687 2.558593 0 5.117187-.976562 7.070312-2.929687 3.90625-3.90625 3.90625-10.238281 0-14.144531l-47.515625-47.515625c17.257813 1.277343 35.421875 4.167969 53.9375 7.160156 7.582031 43.71875 13.089844 85.089844-5.011719 118.3125l-83.433594-83.4375c-3.902343-3.902344-10.234374-3.902344-14.140624 0-3.90625 3.90625-3.90625 10.238281 0 14.144531l85.867187 85.867188c-1.175781 1.3125-2.398437 2.613281-3.679687 3.894531l-.175782.175781c-3.898437 3.910156-3.890625 10.242188.019532 14.140625 1.953124 1.945313 4.507812 2.917969 7.0625 2.917969 2.5625 0 5.128906-.980469 7.082031-2.9375l.164062-.167969c41.113281-41.109375 36.199219-95.464843 27.105469-149.601562 55.082031 8.386719 110.136719 12.363281 150.621094-28.121094 41.941406-41.941406 34.8125-98.542969 25.144531-154.308594 56.132813 8.964844 113.175781 15.988281 152.929687-23.765625 3.90625-3.90625 3.90625-10.238281 0-14.144531zm-173.820312 34.554687c4.257812 24.203126 8.242188 47.777344 8.308594 69.691407l-36.722656-36.71875c-3.90625-3.90625-10.234376-3.90625-14.144532 0-3.902344 3.902343-3.902344 10.234375 0 14.140625l48.699219 48.699218c-2.703125 14.578126-8.191406 28.082032-17.785156 40.144532l-121.097657-121.101563c34.777344-27.957031 82.148438-22.839843 132.742188-14.855469zm-158.496094 164.988282c-4.269531-24.238282-8.257812-47.847656-8.3125-69.789063l37.425782 37.425781c1.953124 1.953126 4.511718 2.929688 7.070312 2.929688 2.5625 0 5.121094-.976562 7.074219-2.929688 3.902343-3.90625 3.902343-10.238281 0-14.140624l-49.386719-49.386719c2.707031-14.546875 8.191406-28.03125 17.769531-40.070313l121.101563 121.105469c-34.777344 27.953125-82.152344 22.839844-132.742188 14.855469zm0 0"></path><path d="m243.515625 315.492188-.097656-.09375c-3.90625-3.90625-10.234375-3.90625-14.140625 0-3.90625 3.902343-3.90625 10.234374 0 14.140624l.09375.09375c1.953125 1.953126 4.511718 2.929688 7.070312 2.929688s5.117188-.976562 7.070313-2.929688c3.90625-3.902343 3.90625-10.234374.003906-14.140624zm0 0"></path><path d="m269.191406 197.121094.097656.09375c1.953126 1.953125 4.511719 2.929687 7.070313 2.929687s5.117187-.976562 7.070313-2.929687c3.90625-3.90625 3.90625-10.238282 0-14.144532l-.09375-.09375c-3.90625-3.90625-10.238282-3.90625-14.144532 0-3.902344 3.90625-3.902344 10.238282 0 14.144532zm0 0"></path></svg></div></div>'
    function make_request(rid, time, idname){
            $.ajax({
                url: "https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD=Get&FORMAT_OBJECT=SearchInfo&RID="+rid,
                async: true,
                success: function(html){
                    var link = "https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD=Get&RID="+rid;
                    if ($('#'+idname).has('a').length ==0){
                        $('#'+idname).html('<a target="_blank" class="blast-link" href="'+link+'"></a>');
                        delete_popover();
                        $('#'+idname+' .blast-link').html(blast_loading_icon);
                        localStorage.setItem(uuid+'-'+idname+'-RID', rid);
                        $('[data-toggle="popover"]').popover();
                    }
                   if (html.indexOf("Status=WAITING") != -1){
                       time = time+5;
                       if (time < 5*12*20){
                           setTimeout('make_request("'+rid+'",'+time.toString()+',"'+idname+'");',5000);
                       }
                       else{
                          delete_popover();
                          $('#'+idname+' .blast-link').html(blast_stopwatch_icon);
                          $('[data-toggle="popover"]').popover();
                       }
                   };
                   if (html.indexOf("Status=READY") != -1){
                        delete_popover();
                        if (html.indexOf("ThereAreHits=yes") != -1){
                            $('#'+idname+' .blast-link').html(blast_ready_icon);
                        }
                        else {
                          $.ajax({
                              url: link,
                              async: true,
                              success: function(html_ready){
                                  if (html_ready.indexOf("Status=FAILED") != -1){
                                      delete_popover();
                                      $('#'+idname+' .blast-link').html(blast_problem_icon);
                                      $('[data-toggle="popover"]').popover();
                                  }
                                  else {
                                    delete_popover();
                                    $('#'+idname+' .blast-link').html(blast_warning_icon);
                                    $('[data-toggle="popover"]').popover();
                                  }
                              },
                              error: function() {
                                delete_popover();
                                $('#'+idname+' .blast-link').html(blast_fail_icon_for_check);
                                $('[data-toggle="popover"]').popover();
                              },
                               fail: function() {
                                          delete_popover();
                                          $('#'+idname+' .blast-link').html(blast_fail_icon_for_check);
                                          $('[data-toggle="popover"]').popover();        
                               }
                            });
                        }
                   };
                   if (html.indexOf("Status=FAILED") != -1){
                        delete_popover();
                        $('#'+idname+' .blast-link').html(blast_problem_icon);
                        $('[data-toggle="popover"]').popover();
                   };
                   if (html.indexOf("Status=UNKNOWN") != -1){
                        delete_popover();
                        $('#'+idname+' .blast-link').html(blast_problem_icon);
                        $('[data-toggle="popover"]').popover();
                   };
                   if ($('#'+idname+' .blast-link').has( "div" ).length == 0) {
                        delete_popover();
                        $('#'+idname+' .blast-link').html(blast_loading_icon);
                        $('[data-toggle="popover"]').popover();
                   };
                },
            error: function() {
              delete_popover();
              $('#'+idname+' .blast-link').html(blast_fail_icon_for_check);
              $('[data-toggle="popover"]').popover();
            },
            fail: function() {
                  delete_popover();
                  $('#'+idname+' .blast-link').html(blast_fail_icon_for_check);
                  $('[data-toggle="popover"]').popover();
            }
            });
		
        };
    function send_sequence(sequence, db, idname){
        $.ajax({
              type: "POST",
              url: "https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi",
              data:"CMD=Put&PROGRAM=blastn&DATABASE="+db+"&QUERY="+sequence,
              headers: {
                      'Content-Type': 'application/x-www-form-urlencoded'
                  },
              async: true,		
              contentType: 'application/x-www-form-urlencoded',
              success: function(html){
		delete_popover();
		$('#'+idname).html(blast_loading_icon);
                $('[data-toggle="popover"]').popover();
                var RID = $('input[name="RID"]', $(html)).val();
                make_request(RID, 0, idname);
              },
              error: function() {
                  delete_popover();
                  $('#'+idname+' .blast-link').html(blast_fail_icon);
                  $('[data-toggle="popover"]').popover();
                },
              fail: function() {
                    delete_popover();
                    $('#'+idname+' .blast-link').html(blast_fail_icon);
                    $('[data-toggle="popover"]').popover();
            }
        });
    };

  function check_blast_reports(){
                var was_alert = false;
                $( ".to-blast-click" ).each(function() {
                    blast_idname = $( this ).attr('data-target');
                    if ((localStorage.getItem(uuid+'-'+blast_idname+'-RID') != '') && (localStorage.getItem(uuid+'-'+blast_idname+'-RID') != null) && (! was_alert)) {
                        var checked = false;
                        var rid = localStorage.getItem(uuid+'-'+blast_idname+'-RID');
                        $.ajax({
                                url: "https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD=Get&FORMAT_OBJECT=SearchInfo&RID="+rid,
                                async: false,
                                success: function(html){
                                    checked = true;
                                    var link = "https://blast.ncbi.nlm.nih.gov/blast/Blast.cgi?CMD=Get&RID="+rid;
                                    delete_popover();
                                    if (html.indexOf("Status=READY") != -1){
                                        if (html.indexOf("ThereAreHits=yes") != -1){
                                            $('#'+blast_idname).html('<a target="_blank" class="blast-link" href="'+link+'"></a>');
                                            $('#'+blast_idname+' .blast-link').html(blast_ready_icon);
                                        }
                                        else {
                                            $.ajax({
                                              url: link,
                                              async: true,
                                              success: function(html_ready){
                                                  if (html_ready.indexOf("Status=FAILED") != -1){
                                                      localStorage.setItem(uuid+'-'+blast_idname+'-RID', '');
                                                  }
                                                  else {
                                                    delete_popover();
                                                    $('#'+blast_idname+' .blast-link').html(blast_warning_icon);
                                                    $('[data-toggle="popover"]').popover();
                                                  }
                                              }
                                           });
                                        }
                                   }
                                   else {
                                        if (html.indexOf("Status=WAITING") != -1){
                                            $('#'+blast_idname).html('<a target="_blank" class="blast-link" href="'+link+'"></a>');
                                            $('#'+blast_idname+' .blast-link').html(blast_loading_icon);
                                            make_request(rid, 5, blast_idname);
                                        }
                                        else {
                                            localStorage.setItem(uuid+'-'+blast_idname+'-RID', '');
                                        }
                                    }
                                }
                        });
                        if ((! checked) && (! was_alert)) {
                            alert('You have some saved Blast results but we cannot load them for some reason. Please, check your Internet connection. If you use Chrome, enable the CORS extension and reload the page.');
                            was_alert = true;
                        }
                    }
                });
          $('[data-toggle="popover"]').popover();
            };
    function delete_popover(){
      $('.popover').remove();
    }
    var status_searching, sequence, db, blast_idname;
          $(document).ready(function($) {
              //clear_active_classes(1);
              setTimeout('check_blast_reports();', 10);

              function clear_active_classes(first_ind){
                    var i, tabcontent, tablinks;
                    // Get all elements with class="tabcontent" and hide them
                    tabcontent = document.getElementsByClassName("tab-pane");
                    for (i = first_ind; i < tabcontent.length; i++) {
                      tabcontent[i].classList.remove("active");
                      tabcontent[i].classList.remove("show");
                      tabcontent[i].classList.remove("fade");
                    }
                    // Get all elements with class="tablinks" and remove the class "active"
                    tablinks = document.getElementsByClassName("ListGroupItem");
                    for (i = first_ind; i < tablinks.length; i++) {
                      tablinks[i].classList.remove("active");
                    }
              }
              function changetab(idname) {
                                // Declare all variables
                                clear_active_classes(0);
                                // Show the current tab, and add an "active" class to the button that opened the tab
                                document.getElementById('tab-'+idname).className += " active";
                                document.getElementById(idname).className += " show active fade";

                              }
              var $th = $('table').find('thead');
              $('.list-group').on('scroll', function() {
                // alert(this.scrollTop);
                $th.css('transform', 'translateY('+ this.scrollTop +'px)');
              });
              $("tr.ListGroupItem").click(function() {
                  changetab($(this).data("href"));
              });
              $('[data-toggle="popover"]').popover();
              $('.accordion-toggle').on("click", function(){
                  var accord_id = '';
                  if ($(this).attr('data-target').indexOf("phage") != -1) {
                    accord_id = $(this).attr('data-target').replace("phage", 'blast');
                  }
                  if ($(this).attr('data-target').indexOf("blast") != -1) {
                    accord_id = $(this).attr('data-target').replace("blast", 'phage');
                  }
                  if (accord_id != '') {
                    if ($(accord_id).hasClass('show') == true){
                        $(accord_id+'-id').click();
                    }
                  }
                 $(this).children('a.arrow').toggleClass('active');
		 document.getElementById('td-'+$(this).attr('data-target').replace('#', '')).parentNode.classList.toggle('show'); 
                 document.getElementById('td-'+$(this).attr('data-target').replace('#', '')).classList.toggle('show');  
              });
              $('.ListGroupItem').on('click', function(){
                 $('#'+$(this).attr('data-href')).html($('#'+$(this).attr('data-href')).children('.prophage-plot').attr('style', '').parent().html());
              });
              $('.download-sequence').on('click', function(){
                  var blob = new Blob([$($(this).attr('data-target')).attr('sequence').replace('%3E', '>').replace(/%0A/g, '\\n')], {type: "text/html;charset=utf-8"});
                  saveAs(blob, 'Prophage_'+$(this).attr('data-target').replace('#accordeon-blast-', '')+'.fasta');
              });
              $('.to-blast-click').on('click',  function() {
                        blast_idname = $(this).attr('data-target');
                        sequence = $('#accordeon-'+blast_idname.replace('-nt', '').replace('-refseq', '')).attr('sequence');
                        db = $(this).attr('db');
                        delete_popover();
           		$('#'+blast_idname).html(blast_waiting_icon);
            		$('[data-toggle="popover"]').popover({html: true, 
							    content:"If loading will not start in 20 sec: <ol><li>Reload page and try again.</li><li>If you use Chrome browser, please, install and/or enable the <a target='_blank' href='https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf?utm_source=chrome-app-launcher-info-dialog'> CORS extension.</a> </li><li>Try another browser. </li><li>Do it manually.</li></ol>"}).on("mouseenter", function () {
                    		var _this = this;
                    		$(this).popover("show");
                    		$(".popover").on("mouseleave", function () {
                       		$(_this).popover('hide');
                    		});
                	}).on("mouseleave", function () {
                    		var _this = this;
                    		setTimeout(function () {
                        		if (!$(".popover:hover").length) {
                            			$(_this).popover("hide");
                        		}
                    		}, 300);
            		});
                        localStorage.setItem(uuid+'-'+blast_idname+'-RID', '');
			 send_sequence(sequence, db, blast_idname);
             });
              $('.to-blast-all').on('click',  function() {
                $('.to-blast-click').click();
            });
              $('.download-sequence-all').on('click',  function() {
                var all_sequences = [];
                $('.accordion-body[sequence]').each(function(indx, element){
                  all_sequences.push($(element).attr('sequence').replace('%3E', '>').replace(/%0A/g, '\\n')+'\\n');
                });
                var blob = new Blob(all_sequences, {type: "text/html;charset=utf-8"});
                saveAs(blob, 'Prophages_all.fasta');
            });
            $(document).on('click', function (e) {
                    var container = $(".xy, .infolayer, .modebar, .table, .do-for-all, .accordion-body, .popover, .td-to-blast, .to-blast-click, .blast-icons, svg, path");
                    if (!container.is(e.target) && container.has(e.target).length === 0 && !($(e.target).prop("tagName")==='svg' || $(e.target).prop("tagName")==='path')) {
                        $('.collapse.show').each(function(indx, element){
                            $('.accordion-toggle[data-target="'+$(element).attr('id').replace('td-', '#')+'"]').click();
                        })
                    }
                });
          });
      </script>
  </body>
  </html> 
  '''
