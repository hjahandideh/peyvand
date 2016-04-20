/*
 *  PURE Rich Text Editor Lite
 *  Created by Kevin Steerment
 *  
 *  Copyright © 2012
 *
 *  Version 1.0.1, last updated 22/06/2012
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
 *  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 *  MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 *  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 *  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
 *  AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 *  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
 *  OF THE POSSIBILITY OF SUCH DAMAGE.
*/

(function($){

	var debugmode = true;

	//Print things to the log and alert problems!
	debugme = function(logthis,alertthis) {
		if (debugmode == true && logthis) { console.log(logthis); }
		if (debugmode == true && alertthis) { alert(alertthis); }
	}

	//function to trigger a click where caret is
	triggerclick = function() {
		debugme('click triggered');
		thiselement = window.getSelection().focusNode.parentNode;
		$(thiselement).trigger('click');
	}
	
	$.fn.cwPureLight = function(options) {

		var editableArea;
		var closetoolbar;
		var buttonson = new Array('start');
		var thistextbox = $(this);

		//Create Unique ID
		if (typeof $.fn.cwPureLight.counter == 'undefined') {
			$.fn.cwPureLight.counter = 1;
		} else {
			$.fn.cwPureLight.counter++;
		}
		var idcounter = $.fn.cwPureLight.counter;

		//Set Defaults
        var defaults = {
			animation:			true,
			buttons:			["bold","italic","underline","insertUnorderedList","href","html"]
        };

		//Merge Options
        var options = $.extend(defaults, options);

		//Create HTML for PRTE
		var purelighthtml = '<div class="pure_rte" prte="'+idcounter+'">' +
					'<div class="prte_toolbar">';
						
						//Add buttons to toolbar in order of array
						for (var i = 0; i < options.buttons.length; i++) {
							if (i == 0) { firstline = " prte_first"; } else { firstline = ""; }
							purelighthtml = purelighthtml + '<div class="prte_button' + firstline + '"><a href="#" command="' + options.buttons[i] + '"></a></div>';
						}

					 purelighthtml = purelighthtml + '</div>' +
					'<div class="prte_editor" contenteditable="true">' + thistextbox.val() + '</div>' +
					'<textarea class="html_editor">' + thistextbox.val() + '</textarea>' +
				'</div>';

		//Create PRTE
		thistextbox.hide();
		thistextbox.after(purelighthtml);
		editableArea = $("[prte='"+idcounter+"'] [contenteditable]");

		if (options.animation == false) {
			$("[prte='"+idcounter+"'] .prte_toolbar").show();
			$("[prte='"+idcounter+"'] .prte_editor").css('marginTop','-6px');
		}

		//Toolbar Animation
		$("[prte='"+idcounter+"'] .prte_editor").focus(function() {
			if (options.animation == true) {
				debugme('open toolbar: '+closetoolbar);
				clearTimeout(closetoolbar);
				$(this).parent().find('.prte_toolbar').slideDown('fast');
				$(this).css('marginTop','-6px');
			}
		});
		$("[prte='"+idcounter+"'] .prte_editor").focusout(function() {
			if (options.animation == true) {
				var $thiseditor = jQuery(this);
				closetoolbar = setTimeout(function() { $thiseditor.parent().find('.prte_toolbar').slideUp('fast'); $thiseditor.css('marginTop','0px'); },100);
			}
		});

		//Make sure editor doesnt disappear when in html mode
		$("[prte='"+idcounter+"'] .html_editor").focus(function() {
			$(this).parent().find('.prte_toolbar').slideDown('fast');
		});

		//Focuising inside contenteditable sets the var(obj) editableArea
		$("[prte='"+idcounter+"'] [contenteditable]").focus(function() {
			editableArea = this;
		});

		//Moving the cursor inside a contenteditable div triggers a click where the cursor is
		$("[prte='"+idcounter+"'] [contenteditable]").keyup(function(e) {
			triggerclick();
		});

		//Clicking on a contenteditable box cleans the toolbar
		$("[prte='"+idcounter+"'] [contenteditable]").click(function() {
			cleantoolbar(idcounter);
		});

		//Save html to hidden textarea
		$("[prte='"+idcounter+"'] [contenteditable]").focusout(function() {
			thistextbox.val($(this).html());
			$("[prte='"+idcounter+"'] .html_editor").val($(this).html());
			$("[prte='"+idcounter+"'] .html_editor").css('height',$(this).height());
		});

		//Disable the A tag in the toolbar for command buttons
		$("[prte='"+idcounter+"'] .prte_button a").click(function(event) {
			event.preventDefault();
		});

		//Remove any 'ON' states from the toolbar
		cleantoolbar = function(idcounter) {
			$("[prte='"+idcounter+"'] [command]").each(function() {
				if (jQuery.inArray($(this).attr('command'), buttonson) > 0) {
					$(this).parent().addClass('prte_on');
				} else {
					$(this).parent().removeClass('prte_on');
				}
			});
			debugme('buttonson = '+buttonson.join(' / ') + ' (toolbar cleaned)');
			buttonson = new Array('start');
		}

		//Toolbar Button 'SET STATE' Function
		buttonstate = function(button,state,idcounter) {
			if (state == 'on') {
				$("[prte='"+idcounter+"'] [command='"+button+"']").parent().addClass('prte_on');
				if (button != 'html') { buttonson.push(button); } //add to button array except for html button ;)
			} else if (state == 'off') {
				$("[prte='"+idcounter+"'] [command='"+button+"']").parent().removeClass('prte_on');
			} else {
				debugme(idcounter + ' is on/off: '+$("[prte='"+idcounter+"'] [command='"+button+"']").parent().hasClass('prte_on'));
				return($("[prte='"+idcounter+"'] [command='"+button+"']").parent().hasClass('prte_on')); //return if button is on (true) or off (false)
			}
		}

		//*************** MONITOR CLICK / CURSOR IN EDITABLE AREA ******************

		$("[prte='"+idcounter+"'] [contenteditable]").delegate("b", "click", function (evt) {
			buttonstate('bold','on',idcounter);
		});

		$("[prte='"+idcounter+"'] [contenteditable]").delegate("u", "click", function (evt) {
			buttonstate('underline','on', idcounter);
		});

		$("[prte='"+idcounter+"'] [contenteditable]").delegate("i", "click", function (evt) {
			buttonstate('italic','on', idcounter);
		});

		$("[prte='"+idcounter+"'] [contenteditable]").delegate("ul", "click", function (evt) {
			buttonstate('insertUnorderedList','on', idcounter);
		});

		$("[prte='"+idcounter+"'] [contenteditable]").delegate("a", "click", function (evt) {
			buttonstate('href','on', idcounter);
		});

		//*************** MONITOR CLICK / CURSOR IN EDITABLE AREA ******************


		//command funciton for all toolbar actions
		$("[prte='"+idcounter+"'] [command]").click(function(thisclick) {
			var value = true;
			var noclass = false;
			var thiscommand = $(this).attr("command");
			debugme(thiscommand);

			if (editableArea == null) { alert('Click an editable area first'); return(false); }

			//update button state
			if (buttonstate(thiscommand,'',idcounter) || noclass) { buttonstate(thiscommand,'off', idcounter); } else { buttonstate(thiscommand,'on', idcounter); }

			//catch if user has pressed view source button
			if (thiscommand == "html") {
				clearTimeout(closetoolbar);
				if (buttonstate(thiscommand,'',idcounter) == true) {
					$("[prte='"+idcounter+"'] [contenteditable]").hide();
					$("[prte='"+idcounter+"'] .html_editor").show();
				} else {
					$("[prte='"+idcounter+"'] [contenteditable]").html($("[prte='"+idcounter+"'] .html_editor").val()); //update html!
					thistextbox.val($("[prte='"+idcounter+"'] .html_editor").val()); //update submitted box
					$("[prte='"+idcounter+"'] [contenteditable]").show();
					$("[prte='"+idcounter+"'] .html_editor").hide();
				}
				return(true);
			}
			
			if (thiscommand == "bold" || thiscommand == "italic" || thiscommand == "underline" || thiscommand == "href") {
				try {
					document.execCommand("styleWithCSS", 0, false);
				} catch (e) {
					try {
						document.execCommand("useCSS", 0, true);
					} catch (e) {
						try {
							document.execCommand('styleWithCSS', false, false);
						}
						catch (e) {
							debugme('Unable to set style formatting.');
						}
					}
				}
			}
			if (thiscommand == "href") { value = prompt("Type a url:","http://"); if (!value) { return(false); } thiscommand = "createLink"; }
			
			clearTimeout(closetoolbar);

			//do command action
			document.execCommand(thiscommand , false, value);
		});

	};

})(jQuery);