

/* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- *
file-name:		framework.js
description:	Minimal JS loaded when initial framework request is made.
last-update:	2015-03-29: Sunday
updated-by:		Patrick Haugen (pathaugen@gmail.com)
* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- */
/* Development helping note in the log */
console.log('START: framework.js');
/* ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- */
/* Loading Velocity.js to replace jQuery's .animate() */
$.getScript('/resources/js/velocity.js', function() {
	console.info('LOADED: velocity.js');
});
/* ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- */
/* Loading Spinner.js as a dynamic vector based animated loading spinner */

/* ---------- ---------- ---------- ---------- ---------- */
/* Spinner Options */
var opts = {
	lines:		8,
    length:		5,
    width:		3,
    radius:		10,
    corners:	1,
    rotate:		0,
    direction:	1,
    color:		'white',
    speed:		1.3,
    trail:		60,
    shadow:		true,
    hwaccel:	true,
    className:	'spinner',
    zIndex:		2e9,
    top:		'50%',
    left:		'50%'
};
/* ---------- ---------- ---------- ---------- ---------- */

/* ---------- ---------- ---------- ---------- ---------- */
/* function to draw spinners and return the object to destroy later */
function spinnerStart(targetId) {
	var spinnerTarget = document.getElementById(targetId);
	var spinner = new Spinner(opts).spin(spinnerTarget);
	return spinner;
}
/* ---------- ---------- ---------- ---------- ---------- */

/* ---------- ---------- ---------- ---------- ---------- */
/* function to destroy a spinner object */
function spinnerStop(targetObject) {
	targetObject.stop();
}
/* ---------- ---------- ---------- ---------- ---------- */

$.getScript('/resources/js/spinner.js', function() {
	console.info('LOADED: spinner.js');
	
	/* ---------- ---------- ---------- ---------- ---------- */
	/* AJAX loading section into the framework.html #section */
	function sectionLoad(section) {
		console.log('AJAX LOADING: '+section);
		
		var loadingSection = spinnerStart(section);
		
		$( '#'+section ).load( '/'+section+'.html', function( response, status, xhr ) {
		    if ( status == "error" ) {
		        spinnerStop(loadingSection);
		        
		        var msg = 'Sorry but there was an error loading '+section+': ';
		        var errorMsg = msg + xhr.status + " " + xhr.statusText;
		        console.error( errorMsg );
		        
		        $( '#'+section ).html('<div class="loading-ajax-error">'+errorMsg+'</div>');
		    } else {
		        spinnerStop(loadingSection);
		        
		        console.info('Successfully AJAX Loaded '+section+'!');
		        
		        /* Upon successful load of HTML: Load the JS file for this section */
		        $.getScript('/resources/js/'+section+'.js', function() {
		        	console.info('LOADED: '+section+'.js');
		        });
		        
		        
		    	/* ---------- ---------- ---------- ---------- ---------- */
		        /* Upon successful load of HTML: Load the CSS file for this section */
		        $('<link/>', {
					rel:	'stylesheet',
					type:	'text/css',
					href:	'/resources/css/'+section+'.css'
		        }).appendTo('head');
		    	/* ---------- ---------- ---------- ---------- ---------- */
		    }
		});
	}
	/* ---------- ---------- ---------- ---------- ---------- */
	
	/* ---------- ---------- ---------- ---------- ---------- */
	/* AJAX loading all sections after the DOM has loaded */
	$(function() {
		sectionLoad('nav');
		sectionLoad('header');
		sectionLoad('content');
		sectionLoad('footer');
	});
	/* ---------- ---------- ---------- ---------- ---------- */
	
});
/* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- */

