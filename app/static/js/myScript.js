/* ========== EDIT-VIEW MODUS ======== */

// Opening edit-view modus

$("#FullWrite-icon-buttom").on("click", function() {
  $("#app-layout-board").css("display", "none");
  $("#journal-toolbar-back").css("display", "block");
  $("#journal-editor-area").css("margin-left", "15%");  
});

// Closing edit-view modus  

$("#journal-toolbar-back").on("click", function() {
  // Showing left-side board
  $("#app-layout-board").css("display", "block");
  // Hiding journal-toolbar-back and editor-toolbar-button
  $("#journal-toolbar-back").css("display", "none");
  $("#journal-editor-area").css("margin-left", "0%");
});

/* ======= GENERAL-ACTIONS MENU =======  */
// Opening general-actions menu   ** Change to JQuery **
var elLogout = document.getElementById('logout-button');
elLogout.addEventListener('click', function() {
  document.getElementById('general-action-menu').style.display = 'block';
}, false);

// Closing general-actions menu
var elNavClose = document.getElementById('general-action-menu');
elNavClose.addEventListener('mouseleave', function() {
  document.getElementById("general-action-menu").style.display = "none";
}, false);


/* ======= CREATING JOURNAL ENTRIES  =========== */

// Button from list area
// Adding eventListener to the button element
$("#list-icon-bton").on('click', function() {

  // Activating edit mode 
  $("#journal-editor-area, #save-button").css("display", "block");                                     // Showing the editor area and save-button     
  $("#journal-list-logo-elements, #logo-holder").css("display", "none");                               // Hiding the editor-area-logo and list-area-logo    
  $("#list-is-empty").removeClass("journal-list-is-empty");
  $("#list-is-empty").addClass("journal-list-is-not-empty");                                            // Changing class attribute od div container            
  $("#journal-editor-area").css("margin-left", "0%");

  // Adding item to the start of the list  editor-toolbar-button
  addEntry();
});

// Button from top-bar area
// Getting the 'add-entry-top-button' 
$("#editor-toolbar-button").on("click", function() {

  // Activating edit mode
  $("#editor-toolbar-button, #edit-button, #delete-button, #view-mode, #logo-holder").css("display", "none"); // .selectable-journal-item, 
  // $("#edit-button, #delete-button").css("display", "none"); // .selectable-journal-item
  $("#save-button, #journal-editor-area").css("display", "block");
  // $("#view-mode").css("display", "none");

  // Adding item to the start of the list 
  addEntry();
});

// Function that adds entry to the list
function addEntry() {
  var $newItemFirstLi = $('<li>').addClass("text-content").text("New Entry...");                        // Create <li> element, add class and text node to it  
  var $newItemFirstBton = $('<button>').prepend($newItemFirstLi);                                       // Create element: <button>  and prepend the list node to it 
  var $selectableDiv = $('<div>').addClass("selectable-journal-item").prepend($newItemFirstBton);       // Create <div> element and prepend the button node to it        
  $("ul").prepend($selectableDiv); //  $selectableDiv                                                    // Getting the <ul> element and adding element to the it
};


/*  ==== Selecting entry items when click it=========== */
// Get <ul> element
// var clickInList = false;                                                                
$("#list-of-journals").on("click", function(e) {                                                       // Add click event listener and pass event object (event delegation) 
  // clickInList = true;
  $target = e.target;                                                                                  // Get event object target: where the click happened  
  var $itemList = $("ul").children(); 
  for (var items = 0; items < $itemList.length; items++ ) {                                            // Iterate over the list 
    if ( $itemList[items] == $target ) {                                                               // If target == element in list
      // console.log(alert("Item " + items + " is target"));
      $itemList[items].className = "selected-item";                                                      // Set class to: 
      var elItemDB = document.getElementsByClassName("selected-item")[0].getAttributeNode('data-item-num').value;
      $(function() {
        $.getJSON('edit_entry', {elItemDB:elItemDB}, function(result) {
          // console.log(alert(result.post.title));                                                        // Print an alert msg with the Title
          // $(".selected-item").attr("data-item-num", result.post.id);                                    // Put id from db into the data-item from entry
          $("#show-head").text(result.post.title);                                                        // Put the title into the entry
          $("#show-body").text(result.post.body)
          // $(".selectable-journal-item").css("display", "block");
        });
      });
    } else {                                                                                                 // Otherwise
      // console.log(alert(items))
      $itemList[items].className = "selectable-journal-item";                                          // Set to:
    }
  }
});

/* === List is not empty and not click event was triggered === */
if ( $("ul").children().length >= 1 ) {                                                                // && clickInList == false                                         
  var $entryList =  $("ul").children();
  $entryList[0].className = 'selected-item';
  $("#save-button, #journal-list-logo-elements, #logo-holder").css("display", "none");
  $("#edit-button, #delete-button, #view-mode").css("display", "block");
  var elItemDB = document.getElementsByClassName("selected-item")[0].getAttributeNode('data-item-num').value;
  $(function() {
    $.getJSON('edit_entry', {elItemDB:elItemDB}, function(result) {
      // console.log(alert(result.post.title));                                                        // Print an alert msg with the Title
      // $(".selected-item").attr("data-item-num", result.post.id);                                    // Put id from db into the data-item from entry
      $("#show-head").text(result.post.title);                                                        // Put the title into the entry
      $("#show-body").text(result.post.body)
      // $(".selectable-journal-item").css("display", "block");
    });
  });
  // $("#delete-button").css("display", "block");
} else {
  $("#editor-toolbar-button").css("display", "none");
  // $('.journal-list-theme').css("display", "block");
  $(".edit-button, .delete-button, .save-button").css("display", "none");
}
 
/* ============== Mutations in the DOM =============
==================================================== */
// Options for the observer (which mutations to observe)
var elList = document.getElementById("list-of-journals");
const config = {childList: true}; // attribute: true, 

const callback = function (mutationsList) {          
  mutationsList.forEach(function (mutation) {
    if (mutation.addedNodes.length) {      
      // console.log(alert(mutation.addedNodes[0]))
      var $itemList = $("ul").children();
      if ($itemList.length > 1) {
        for (var items = 1; items < $itemList.length; items++) {
          // console.log(alert($itemList.length))
          $itemList[items].className = "selectable-journal-item";
          $(".selectable-journal-item").css("display", "none");                    
        }
      }
      mutation.addedNodes[0].className = "selected-item";
      mutation.addedNodes[0].style.display = "block";
    }
  });
}; 

// Creater an observer instance linked to the callback function
const observer = new MutationObserver(callback);

// Start observing the target node for configured mutations
observer.observe(elList, config);

/* ===========WRITING TITlE========================
================================================= */

// Getting entry in the editor header
var elTitle = document.getElementById('journal-editor-header');
// Adding Listener to the keyup
/* elTitle.addEventListener('keyup', function(e) {
  target = e.target;
  textEntered = target.innerText;
  // Getting text node of selected-item
  var elSelectedEntry = document.getElementsByClassName('selected-item')[0];
  elSelectedEntry.contentEditable = 'true';
  var elFirst = elSelectedEntry.firstChild;
  var elSecond = elFirst.firstChild;
  elSecond.textContent = textEntered;
}, false); */

/* ===========SAVE FUNCTION================
============================================== */
// Getting save-button 
 $('#save-button').on('click', function() {
   
  // Get content of the header (title) editor:
  var elTitle = tinymce.get('journal-editor-header').getContent({format: 'text'});
  // Get content of the body editor:
  var elBody = tinymce.get('journal-editor-body').getContent({format: 'text'}); 

  // Save request to the server 
  $.ajax({
    url:'save_journal',
    type: 'POST',
    data: {
     elTitle: elTitle,
     elBody: elBody
    }
  });
  // Loading last entry from db into the list of entries
  $(function() {
    $.getJSON("loading_entry", function(result) {                                          // Get last entry from database using $.getJSON() method
      // console.log(alert(JSON.stringify(result)));
      // console.log(alert(result.post[0]["id"])); 
      $(".selected-item").attr("data-item-num", result.post[0]["id"]);                     // Put id from db into the data-item from entry
      $(".selected-item").find("li").text(result.post[0]["title"]);                        // Put the title into the entry
      $("#show-head").text(result.post[0]["title"]);                                       // Put the title into the entry-head-view
      $("#show-body").text(result.post[0]["body"])
    });
  });
  // Empty the editor
  tinymce.get('journal-editor-header').setContent('Title');                                 
  tinymce.get('journal-editor-body').setContent('');

  // Activate view mode
  $('#journal-editor-area, #save-button').css("display", "none"); 
  $('#editor-toolbar-button, #view-mode, #edit-button, #delete-button, .selectable-journal-item').css("display", "block");  
  // $("#save-button").css("display", "none");    // Hide save-button
  // Show edit and delete-button
  // $("#edit-button").css("display", "block");
  // $("#delete-button").css("display", "block");
  // $(".selectable-journal-item").css("display", "block");
});

/*============ EDIT FUNCTION =======================
===================================================*/
$("#edit-button").on("click", function() {
  // Getting the item num in db
  var elItemDB = document.getElementsByClassName("selected-item")[0].getAttributeNode('data-item-num').value;
  // console.log(alert(elItemDB))
  $("#delete-button, #edit-button, .selectable-journal-item, #app-layout-board, #editor-toolbar-button, #view-mode").css("display", "none");
  $(".submit-button, #journal-toolbar-back").css("display", "block");
  $("#journal-editor-area").css("margin-left", "15%");
  // 
  $(function() {
    $.getJSON("edit_entry", {elItemDB:elItemDB}, function(result) {
      // console.log(alert(result.post.title))
      $("#journal-editor-area").css("display", "block");
      tinymce.get('journal-editor-header').setContent(result.post.title);
      tinymce.get('journal-editor-body').setContent(result.post.body);
    });
  });  
});
/* ================================================================================ */

// DELETE REQUEST-FUCTION 
$('.delete-button').on('click', function() {
    // Getting the item num in db
    var elItemDB = document.getElementsByClassName("selected-item")[0].getAttributeNode('data-item-num').value;
    // clickInList = false    
    // Sending delete request to the server
    $.ajax({
      url:'delete_entry',
      type: 'POST',
      data: {
        elItemDB:elItemDB
      }
    });
    $('.selected-item').remove();
    var $itemList = $("ul").children();  
    if ($itemList.length >= 1 ) {                                  // && clickInList == false
      $itemList[0].className = 'selected-item';
      $("#save-button").css("display", "none");
      $("#edit-button, .delete-button").css("display", "block");
      $(function() {
        var elItemDB = document.getElementsByClassName("selected-item")[0].getAttributeNode('data-item-num').value;
        $.getJSON('edit_entry', {elItemDB:elItemDB}, function(result) {
          console.log(alert(elItemDB));
          console.log(alert(result.post.title));                                                           // Print an alert msg with the Title
          // $(".selected-item").attr("data-item-num", result.post.id);                                    // Put id from db into the data-item from entry
          $("#show-head").text(result.post.title);                                                        // Put the title into the entry
          $("#show-body").text(result.post.body)
          // $(".selectable-journal-item").css("display", "block");
        });
      });
    } else {
      $("#editor-toolbar-button").css("display", "none");
      $("#journal-list-logo-elements").css("display", "block");
      $("#edit-button, #delete-button, #save-button, #view-mode").css("display", "none");
    } 
}); 

/* =============== Submit Function ==============
  ===============================================  */

  // Getting submit-button 
 $('#submit-button').on('click', function() {
   // Hide save-button
   $("#submit-button, #journal-toolbar-back").css("display", "none");
   // Show edit and delete-button
   $("#edit-button, #app-layout-board, #delete-button, #view-mode").css("display", "block");
   // $("#delete-button").css("display", "block");

   // Get content of the header (title) editor:
   var elTitle = tinymce.get('journal-editor-header').getContent({format: 'text'});
   // Get content of the body editor:
   var elBody = tinymce.get('journal-editor-body').getContent({format: 'text'});
   // Get id number of the entry
   var elItemDB = document.getElementsByClassName("selected-item")[0].getAttributeNode('data-item-num').value;
   // Activate view mode
   document.getElementById('journal-editor-area').style.display = 'none';
   document.getElementById('editor-toolbar-button').style.display = 'block';

   // Submit-change request to the server 
   $.ajax({
     url:'submit_change',
     type: 'POST',
     data: {
     elTitle: elTitle,
     elBody: elBody,
     elItemDB: elItemDB
    }
  });
  tinymce.get('journal-editor-header').setContent('Title'); // Setting...
  tinymce.get('journal-editor-body').setContent('');
  
  // Update entry in the list-side-bar 
  $(function() {
    $.getJSON('loading_change', {elItemDB:elItemDB}, function(result) {
      // console.log(alert(result.post.title));                                                    // Print an alert msg with the Title
      $(".selected-item").attr("data-item-num", result.post.id);                                // Put id from db into the data-item from entry
      $(".selected-item").find("li").text(result.post.title);                                   // Put the title into the entry
      $(".selectable-journal-item").css("display", "block");
    });
  });
});