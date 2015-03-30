

/* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- *
file-name:		footer.js
description:	JS supporting the content.
last-update:	2015-03-29: Sunday
updated-by:		Patrick Haugen (pathaugen@gmail.com)
* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- */
console.log('START: footer.js');
/* ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- */
/* Function to AJAX request pages and store into a cache for using in place of AJAX requests */
var popupCache = {};
function getPopup(thisUrl) {
	/* Strip down thisURL to just the page requested via regex */
	thisPage = thisUrl.replace( /(^.*\/)/g, '');
	
	var loadingPopup = spinnerStart('blackout');
	console.log('LOADING: Starting load for '+thisUrl);
    $( 'body' ).css({'cursor':'progress'});
    
    if (thisUrl in popupCache) {
        spinnerStop(loadingPopup);
        
    	console.info('LOADED: Successfully JS CACHE Loaded '+thisUrl+'!');
    	
        $( '#popup' ).html( popupCache[thisUrl] ).velocity({'top':'50px','bottom':'50px'});
        $( '#blackout' ).html('<a href="">Close Popup</a>');
        $( 'body' ).css({'cursor':'auto'});
    } else {
        $( '#popup' ).load( '/resources/html/'+thisUrl+'.html', function( response, status, xhr ) {
            if ( status == "error" ) {
		        spinnerStop(loadingPopup);
		        $( '#blackout' ).hide();
                
                var msg = "Sorry but there was an error: ";
                var errorMsg = msg + xhr.status + " " + xhr.statusText;
		        console.error( errorMsg );
                
                $( 'body' ).css({'cursor':'auto'});
            } else {
		        spinnerStop(loadingPopup);
		        
            	console.info('LOADED: Successfully AJAX Loaded '+thisUrl+'!');
                
            	popupCache[thisUrl] = $( '#popup' ).html();

                $( '#popup' ).velocity({'top':'50px','bottom':'50px'});
                $( '#blackout' ).html('<a href="">Close Popup</a>');
                $( 'body' ).css({'cursor':'auto'});
            }
        });
    }
}
/* ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- */
$(function() {
	

	/* Stop the default click behavior of the nav menu */
    $( '#footer ul li' ).on('click', 'a', function() {
        event.preventDefault();
        
        $( '#blackout' ).show();
        
        thisUrl = $(this).prop('href');
        
        window.history.pushState("pushState string/object", "pushState Title", thisUrl);

        getPopup(thisUrl);
    });
    
    
	/* Stop the default click behavior of the blackout link */
    $( '#blackout' ).on('click', 'a', function() {
        event.preventDefault();

        $( '#popup' ).velocity({'top':'100%','bottom':'-100%'});
        $( '#blackout' ).hide();
    });
    
    
});
/* ---------- ---------- ---------- ---------- ---------- */

