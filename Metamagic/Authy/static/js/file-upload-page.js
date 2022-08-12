const dragArea = document.querySelector('#box');
const dragText = document.querySelector('.dragtext');

let dropClick = document.querySelector(".box-content");
let input = document.querySelector('.drop_input');

let file;

dropClick.onclick = () => {
	input.click();

};

//when browse
input.addEventListener('change', function () {
	file = this.files[0];
	dragArea.classList.add('actives');
	displayFile();


});


//when file is in the drag area
dragArea.addEventListener('dragover', (event) => {
	event.preventDefault();
	dragText.textContent = 'Release to upload';
	dragArea.classList.add('actives');
	//console.log("file is inside the drag area");
})

//when file leaves the drag area
dragArea.addEventListener('dragleave', (event) => {
	event.preventDefault();
	dragText.textContent = 'Drag and drop a file here';
	dragArea.classList.remove('actives');
	//console.log('file left the drag area');
})

//when the file is dropped

dragArea.addEventListener('drop', (event) => {
	event.preventDefault();
	
	file = event.dataTransfer.files[0];
	//console.log(file);
	displayFile();

		
});

function displayFile() {
	let fileType = file.type;

	//console.log('file has been dropped');
	let validExtensions = ['image/jpeg', 'image/jpg', 'image/png', 'image/svg', 'image/svg+xml', 'application/pdf', 'application/json', 'text/csv', 'video/mp4',];

	if(validExtensions.includes(fileType)) {
		let fileReader = new FileReader();
	

		fileReader.onload = () => {
			let fileURL = fileReader.result;
			console.log(fileURL);
		};
		fileReader.readAsDataURL(file);
	} else {
		alert('File type not supported');
		dragArea.classList.remove('active')

	}

	
	
	//console.log('file has been dropped');

}