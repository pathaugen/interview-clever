

/* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- *
file-name:		clever.js
description:	JS supporting the clever page.
last-update:	2015-03-29: Sunday
updated-by:		Patrick Haugen (pathaugen@gmail.com)
* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- */
console.log('START: clever.js');
/* ---------- ---------- ---------- ---------- ---------- */


/* ---------- ---------- ---------- ---------- ---------- */
$(function() {
	
	/* ---------- ---------- ---------- ---------- ---------- */
	/* Event listener for click on .district */
    $( '#content' ).on('click', '.district', function() {
    	if ( !($(this).attr('clicked')) ) {
            $(this).attr('clicked',true);
	    	$(this).css({'cursor':'default'});
	    	/* ---------- ---------- ---------- ---------- ---------- */
	    	var districtId = $('.district-id',this).html().replace( /(^.* )/g, '');
	    	var posting = $.post( '/clever/post', {
	    		cleverdistrict: districtId
	        });
	        posting.done(function( data ) {
	        	$('.district-details').html(data);
	        });
	        posting.fail(function( data ) {
	        	$('.district-details').html(data);
	        });
	        posting.always(function () {
	        	console.log('AJAX Loaded: District details');
	        });
	        /* ---------- ---------- ---------- ---------- ---------- */
    	}
    });
    /* ---------- ---------- ---------- ---------- ---------- */
    
    /* ---------- ---------- ---------- ---------- ---------- */
	/* Event listener for click on .district .district-link */
    $( '#content' ).on('click', '.district .district-link', function() {
    	if ( !($(this).attr('clicked')) ) {
	    	$('.district-section').hide();
	    	$('.district-link').removeAttr('clicked');
	    	$('.district-link').removeClass('district-link-selected');
	    	
            $(this).attr('clicked',true);
            $(this).addClass('district-link-selected');
	    	
	    	var districtUri = $('.district-uri',this).html().replace( /(^.* )/g, '');
	    	var districtUriType = districtUri.replace( /(^.*\/)/g, '');
	    	
	    	/* Check if the div has already been created, and if so show it instead of drawing again */
	    	if ($('#district-'+districtUriType)[0]) {
	    		$('#district-'+districtUriType).show();
	        	console.log('JS CACHE Loaded: District '+districtUriType);
	    	}
	    	else {
		    	$('#content').append('<div class="district-section" id="district-'+districtUriType+'"></div>');
		    	/* ---------- ---------- ---------- ---------- ---------- */
		    	var posting = $.post( '/clever/post', {
		    		cleverdistrictlink: districtUri
		        });
		        posting.done(function( data ) {
		        	$('#district-'+districtUriType).html(data);
		        });
		        posting.fail(function( data ) {
		        	$('#district-'+districtUriType).html(data);
		        });
		        posting.always(function () {
		        	console.log('AJAX Loaded: District '+districtUriType);
		        });
		        /* ---------- ---------- ---------- ---------- ---------- */
	    	}
    	}
    });
    /* ---------- ---------- ---------- ---------- ---------- */
    
    
    /* ---------- ---------- ---------- ---------- ---------- */
	/* Event listener for click on .school */
    /* UPDATED: Loads in #popup instead of .school-details */
    $( '#content' ).on('click', '.school', function() {
    	/*if ( !($(this).attr('clicked')) ) { */
    	/* $('.school').removeAttr('clicked'); */
    	/* $('.school').removeClass('school-selected'); */
    	/* $('.school-details','.school').html('Click to AJAX load details'); */
    	
        /* $(this).attr('clicked',true); */
        /* $(this).addClass('school-selected'); */
        
    	
    	var schoolId = $('.school-id',this).html().replace( /(^.* )/g, '');
    	
        $( '#blackout' ).show();
        var loadingPopup = spinnerStart('blackout');
    	console.log('LOADING: Starting popup load for school: '+schoolId);
        $( 'body' ).css({'cursor':'progress'});
        
    	
    	/* var schoolDetails = $('.school-details',this); */
    	/* ---------- ---------- ---------- ---------- ---------- */
    	var posting = $.post( '/clever/post', {
    		cleverschool: schoolId
        });
        posting.done(function( data ) {
        	/* schoolDetails.html(data); */
        	
        	
        	console.info('LOADED: Successfully AJAX Loaded school: '+schoolId);
        	
        	$( '#popup' ).html(data);

            $( '#popup' ).velocity({'top':'50px','bottom':'50px'});
            $( '#blackout' ).html('<a href="">Close Popup</a>');
        });
        posting.fail(function( data ) {
        	/* schoolDetails.html(data); */
        	
        	
	        $( '#blackout' ).hide();
            
            var msg = "Sorry but there was an error: ";
            var errorMsg = msg + xhr.status + " " + xhr.statusText;
	        console.error( errorMsg );
        });
        posting.always(function () {
        	/*console.log('AJAX Loaded: School details: '+schoolId); */
        	
        	
	        spinnerStop(loadingPopup);
	        
            $( 'body' ).css({'cursor':'auto'});
        });
        /* ---------- ---------- ---------- ---------- ---------- */
    });
    /* ---------- ---------- ---------- ---------- ---------- */
    
    
    /* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- */
    
    /* ---------- ---------- ---------- ---------- ---------- */
    /* Function to take student or teacher ids and return into the popup */
    var popupPersonCache = {};
    function pushPersonPopup(personId,personType) {
    	
    	var loadingPopup = spinnerStart('blackout');
    	console.log('LOADING: Starting popup load for '+personType);
        $( 'body' ).css({'cursor':'progress'});
        
        if (personId in popupPersonCache) {
            spinnerStop(loadingPopup);
            
        	console.info('LOADED: Successfully JS CACHE Loaded '+personType+': '+personId);
        	
            $( '#popup' ).html( popupCache[personId] ).velocity({'top':'50px','bottom':'50px'});
            $( '#blackout' ).html('<a href="">Close Popup</a>');
            $( 'body' ).css({'cursor':'auto'});
        } else {
	    	/* ---------- ---------- ---------- ---------- ---------- */
        	if (personType == 'student') {
		    	var posting = $.post( '/clever/post', {
		    		cleverstudent: personId
		        });
        	}
        	if (personType == 'teacher') {
		    	var posting = $.post( '/clever/post', {
		    		cleverteacher: personId
		        });
        	}
	        posting.done(function( data ) {
            	console.info('LOADED: Successfully AJAX Loaded '+personType+': '+personId);
                
            	$( '#popup' ).html(data);
            	popupPersonCache[personId] = $( '#popup' ).html();

                $( '#popup' ).velocity({'top':'50px','bottom':'50px'});
                $( '#blackout' ).html('<a href="">Close Popup</a>');
	        });
	        posting.fail(function( data ) {
		        $( '#blackout' ).hide();
                
                var msg = "Sorry but there was an error: ";
                var errorMsg = msg + xhr.status + " " + xhr.statusText;
		        console.error( errorMsg );
	        });
	        posting.always(function () {
		        spinnerStop(loadingPopup);
		        
                $( 'body' ).css({'cursor':'auto'});
	        });
	        /* ---------- ---------- ---------- ---------- ---------- */
        }
    }
    /* ---------- ---------- ---------- ---------- ---------- */
    
    /* ---------- ---------- ---------- ---------- ---------- */
    /* When clicking a student */
    $( '#content' ).on('click', '.student', function() {
        $( '#blackout' ).show();

        var personId = $('.student-id',this).html().replace( /(^.* )/g, '');

        pushPersonPopup(personId,'student');
    });
    /* ---------- ---------- ---------- ---------- ---------- */
    
    /* ---------- ---------- ---------- ---------- ---------- */
    /* When clicking a teacher */
    $( '#content' ).on('click', '.teacher', function() {
        $( '#blackout' ).show();
        
        var personId = $('.teacher-id',this).html().replace( /(^.* )/g, '');

        pushPersonPopup(personId,'teacher');
    });
    /* ---------- ---------- ---------- ---------- ---------- */
    
    /* ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- */
    
    
});
/* ---------- ---------- ---------- ---------- ---------- */

