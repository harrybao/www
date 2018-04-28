tinymce.init({
	selector:"textarea",
	themes:"advanced",
	forced_root_block:'',
	menubar:true,
	convert_urls:false,
	height:450,
	width:900,
	plugins:[
		'advlist autolink lists link image charmap print preview hr anchor pagebreak',
        'searchreplace wordcount visualblocks visualchars code fullscreen',
        'insertdatetime media nonbreaking save table contextmenu directionality',
        'emoticons template paste textcolor colorpicker textpattern imagetools',
	],
	 toolbar: "undo redo | imageupload link | bold italic | styleselect fontselect fontsizeselect | bullist numlist outdent indent | alignleft aligncenter alignright alignjustify | print preview media | forecolor backcolor emoticons",
    language:'zh-cn'
});