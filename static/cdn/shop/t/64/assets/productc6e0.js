function maxLength(el){if(!("maxLength"in el)){var max=el.attributes.maxLength.value;el.onkeypress=function(){if(this.value.length>=max)return!1}}}maxLength(document.getElementById("front_text"));function personalise(){tafValue=document.getElementById("front_text").value,tafValue=tafValue.replace(/\n/g,"<br/>"),document.getElementById("front").innerHTML=tafValue,talValue=document.getElementById("left_text").value,document.getElementById("font_preview_left").innerHTML=talValue,talValue=talValue.replace(/\n/g,"<br/>"),document.getElementById("inside_left").innerHTML=talValue,document.getElementById("inside_left_1").innerHTML=talValue,document.getElementById("inside_left_mobile").innerHTML=talValue,tarValue=document.getElementById("right_text").value,document.getElementById("font_preview_right").innerHTML=tarValue,tarValue=tarValue.replace(/\n/g,"<br/>"),document.getElementById("inside_right").innerHTML=tarValue,document.getElementById("inside_right_1").innerHTML=tarValue,document.getElementById("inside_right_mobile").innerHTML=tarValue}$("#inside-left-font").change(function(){inside_left.style.fontFamily=this.value,inside_left_1.style.fontFamily=this.value,inside_left_mobile.style.fontFamily=this.value,font_preview_left.style.fontFamily=this.value;var fontl=this.value;fontl=="Jura"?(inside_left.style.letterSpacing="-0.055em",inside_left_1.style.letterSpacing="-0.055em",inside_left_mobile.letterSpacing="-0.055em",font_preview_left.style.letterSpacing="-0.055em"):(inside_left.style.letterSpacing="0px",inside_left_1.style.letterSpacing="0px",inside_left_mobile.letterSpacing="0px",font_preview_left.style.letterSpacing="0px")}),$("#inside-right-font").change(function(){inside_right.style.fontFamily=this.value,inside_right_1.style.fontFamily=this.value,inside_right_mobile.style.fontFamily=this.value,font_preview_right.style.fontFamily=this.value;var fontr=this.value;fontr=="Jura"?(inside_right.style.letterSpacing="-0.055em",inside_right_1.style.letterSpacing="-0.055em",inside_right_mobile.letterSpacing="-0.055em",font_preview_right.style.letterSpacing="-0.055em"):(inside_right.style.letterSpacing="0px",inside_right_1.style.letterSpacing="0px",inside_right_mobile.letterSpacing="0px",font_preview_right.style.letterSpacing="0px")}),$("#left-font-size").change(function(){var fontsizel=this.value;fontsizel=="Extra-Small"?(inside_left.style.fontSize="15px",inside_left.style.lineHeight="15px",inside_left_1.style.fontSize="15px",inside_left_1.style.lineHeight="15px",inside_left_mobile.style.fontSize="15px",inside_left_mobile.style.lineHeight="15px",font_preview_left.style.fontSize="15px"):fontsizel=="Small"?(inside_left.style.fontSize="18px",inside_left.style.lineHeight="18px",inside_left_1.style.fontSize="18px",inside_left_1.style.lineHeight="18px",inside_left_mobile.style.fontSize="18px",inside_left_mobile.style.lineHeight="18px",font_preview_left.style.fontSize="18px"):fontsizel=="Medium"?(inside_left.style.fontSize="21px",inside_left.style.lineHeight="21px",inside_left_1.style.fontSize="21px",inside_left_1.style.lineHeight="21px",inside_left_mobile.style.fontSize="21px",inside_left_mobile.style.lineHeight="21px",font_preview_left.style.fontSize="21px"):fontsizel=="Large"?(inside_left.style.fontSize="24px",inside_left.style.lineHeight="24px",inside_left_1.style.fontSize="24px",inside_left_1.style.lineHeight="24px",inside_left_mobile.style.fontSize="24px",inside_left_mobile.style.lineHeight="24px",font_preview_left.style.fontSize="24px"):fontsizel=="Extra-Large"?(inside_left.style.fontSize="29px",inside_left.style.lineHeight="29px",inside_left_1.style.fontSize="29px",inside_left_1.style.lineHeight="29px",inside_left_mobile.style.fontSize="29px",inside_left_mobile.style.lineHeight="29px",font_preview_left.style.fontSize="29px"):fontsizel=="XX-Large"?(inside_left.style.fontSize="32px",inside_left.style.lineHeight="32px",inside_left_1.style.fontSize="32px",inside_left_1.style.lineHeight="32px",inside_left_mobile.style.fontSize="32px",inside_left_mobile.style.lineHeight="32px",font_preview_left.style.fontSize="32px"):(inside_left.style.fontSize="21px",inside_left.style.lineHeight="21px",inside_left_1.style.fontSize="21px",inside_left_1.style.lineHeight="21px",inside_left_mobile.style.fontSize="21px",inside_left_mobile.style.lineHeight="21px",font_preview_left.style.fontSize="21px")}),$("#right-font-size").change(function(){var fontsizer=this.value;fontsizer=="Extra-Small"?(inside_right.style.fontSize="15px",inside_right.style.lineHeight="15px",inside_right_1.style.fontSize="15px",inside_right_1.style.lineHeight="15px",inside_right_mobile.style.fontSize="15px",inside_right_mobile.style.lineHeight="15px",font_preview_right.style.fontSize="15px"):fontsizer=="Small"?(inside_right.style.fontSize="18px",inside_right.style.lineHeight="18px",inside_right_1.style.fontSize="18px",inside_right_1.style.lineHeight="18px",inside_right_mobile.style.fontSize="18px",inside_right_mobile.style.lineHeight="18px",font_preview_right.style.fontSize="18px"):fontsizer=="Medium"?(inside_right.style.fontSize="21px",inside_right.style.lineHeight="21px",inside_right_1.style.fontSize="21px",inside_right_1.style.lineHeight="21px",inside_right_mobile.style.fontSize="21px",inside_right_mobile.style.lineHeight="21px",font_preview_right.style.fontSize="21px"):fontsizer=="Large"?(inside_right.style.fontSize="24px",inside_right.style.lineHeight="24px",inside_right_1.style.fontSize="24px",inside_right_1.style.lineHeight="24px",inside_right_mobile.style.fontSize="24px",inside_right_mobile.style.lineHeight="24px",font_preview_right.style.fontSize="24px"):fontsizer=="Extra-Large"?(inside_right.style.fontSize="29px",inside_right.style.lineHeight="29px",inside_right_1.style.fontSize="29px",inside_right_1.style.lineHeight="29px",inside_right_mobile.style.fontSize="29px",inside_right_mobile.style.lineHeight="29px",font_preview_right.style.fontSize="29px"):fontsizer=="XX-Large"?(inside_right.style.fontSize="32px",inside_right.style.lineHeight="32px",inside_right_1.style.fontSize="32px",inside_right_1.style.lineHeight="32px",inside_right_mobile.style.fontSize="32px",inside_right_mobile.style.lineHeight="32px",font_preview_right.style.fontSize="32px"):(inside_right.style.fontSize="21px",inside_right.style.lineHeight="21px",inside_right_1.style.fontSize="21px",inside_right_1.style.lineHeight="21px",inside_right_mobile.style.fontSize="21px",inside_right_mobile.style.lineHeight="21px",font_preview_right.style.fontSize="21px")}),$("input[name='properties[Photo Upload]']").click(function(){$("#file_upload").css("display",$(this).val()==="Yes"?"block":"none")}),$("#photo_no").click(function(){document.getElementById("photo").value=""}),$("#next_button_1").click(function(){return $("#second").click(),!1}),$("#next_button_1").click(function(){$("html, body").animate({scrollTop:$("#pesonalisation").offset().top-0},100)}),$("#next_button_2").click(function(){return $("#third").click(),!1}),$("#next_button_2").click(function(){$("html, body").animate({scrollTop:$("#pesonalisation").offset().top-0},100)}),$("#next_button_3").click(function(){return $("#forth").click(),!1}),$("#next_button_3").click(function(){$("html, body").animate({scrollTop:$("#pesonalisation").offset().top-0},100)}),$("#next_button_4").click(function(){return $("#first").click(),!1}),$("#next_button_4").click(function(){$("html, body").animate({scrollTop:$("#pesonalisation").offset().top-0},100)}),$("#first, #second, #third, #forth").click(function(){$("html, body").animate({scrollTop:$("#pesonalisation").offset().top-0},100)}),$("#scroll").click(function(){$("html, body").animate({scrollTop:$("#pesonalisation").offset().top-0},1e3)}),$("#scroll-delivery").click(function(){return $("html, body").animate({scrollTop:$(".tabs__nav").offset().top-0},500),$("#delivery-tab").click(),!1}),$(".jdgm-preview-badge").click(function(){return $("html, body").animate({scrollTop:$(".tabs__nav").offset().top-0},500),$("#reviews-tab").click(),!1});var modall=document.getElementById("preview_mobile_left"),btnl=document.getElementById("preview_left"),spanl=document.getElementsByClassName("closel")[0];btnl.onclick=function(){modall.style.display="block"},spanl.onclick=function(){modall.style.display="none"},window.onclick=function(event){event.target==modall&&(modall.style.display="none")};var modalr=document.getElementById("preview_mobile_right"),btnr=document.getElementById("preview_right"),spanr=document.getElementsByClassName("closer")[0];btnr.onclick=function(){modalr.style.display="block"},spanr.onclick=function(){modalr.style.display="none"},window.onclick=function(event){event.target==modalr&&(modalr.style.display="none")};
//# sourceMappingURL=/cdn/shop/t/64/assets/product.js.map?v=5954578091427852681681915571