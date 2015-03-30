

/* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- *
file-name:		nav.js
description:	JS supporting the nav menu.
last-update:	2015-03-29: Sunday
updated-by:		Patrick Haugen (pathaugen@gmail.com)
* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- */
console.log('START: nav.js');
/* ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- */
/* Function to AJAX request pages and store into a cache for using in place of AJAX requests */
var pageCache = {};
function getPage(thisUrl) {
	/* Strip down thisURL to just the page requested via regex */
	thisPage = thisUrl.replace( /(^.*\/)/g, '');
	
	var loadingPage = spinnerStart('content');
	console.log('LOADING: Starting load for '+thisUrl);
    $( 'body' ).css({'cursor':'progress'});
    
    if (thisUrl in pageCache) {
        spinnerStop(loadingPage);
        
    	console.info('LOADED: Successfully JS CACHE Loaded '+thisUrl+'!');
    	
        $( '#content' ).html( pageCache[thisUrl] );
        $( 'body' ).css({'cursor':'auto'});
    } else {
        $( '#content' ).load( '/'+thisPage, function( response, status, xhr ) {
            if ( status == "error" ) {
		        spinnerStop(loadingPage);
                
                var msg = "Sorry but there was an error: ";
                var errorMsg = msg + xhr.status + " " + xhr.statusText;
		        console.error( errorMsg );
                
                $( 'body' ).css({'cursor':'auto'});
            } else {
		        spinnerStop(loadingPage);
		        
            	console.info('LOADED: Successfully AJAX Loaded '+thisUrl+'!');
                
                pageCache[thisUrl] = $( '#content' ).html();
                

                /* ---------- ---------- ---------- ---------- ---------- */
                /* Load the JS for the requested URL */
            	console.log('LOADING: Starting load for '+thisPage+'.js');
                $.getScript('/resources/js/'+thisPage+'.js', function() {
                	console.info('LOADED: '+thisPage+'.js');
                });
                /* ---------- ---------- ---------- ---------- ---------- */
                

		    	/* ---------- ---------- ---------- ---------- ---------- */
		        /* Load the CSS for the requested URL */
		        $('<link/>', {
					rel:	'stylesheet',
					type:	'text/css',
					href:	'/resources/css/'+thisPage+'.css'
		        }).appendTo('head');
		    	/* ---------- ---------- ---------- ---------- ---------- */
                
                
                $( 'body' ).css({'cursor':'auto'});
            }
        });
    }
}
/* ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- */
$(function() {
	
	
	/* Stop the default click behavior of the nav menu */
    $( '#nav ul li' ).on('click', 'a', function() {
        event.preventDefault();
        
        thisUrl = $(this).prop('href');
        /* thisPage = thisUrl.replace( /(^.*\/)/g, ''); */
        
        window.history.pushState("pushState string/object", "pushState Title", thisUrl);

        getPage(thisUrl);
    });
    
    
});
/* ---------- ---------- ---------- ---------- ---------- */

