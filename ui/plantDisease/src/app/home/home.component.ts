import { Component, OnInit } from '@angular/core';

import { ServiceService } from '../service/service.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  file: any;

  plantName: any = "Upload Image";
  plantDisease: any = "Upload Image";
  cureSteps: any[] | undefined;
  link: any = "Upload Image";

  constructor(private fileUploadService: ServiceService) {  }

  ngOnInit(): void {
  }

  onChange(event: any) {
    this.file = event.target.files[0];
    var image = <HTMLInputElement>document.getElementById('blah');
	  image.src = URL.createObjectURL(this.file);
    console.log(image.src);
  }

  // OnClick of button Upload
  onUpload() {
    this.plantName = "Upload Image";
    this.plantDisease = "Upload Image";
    this.cureSteps = [];
    this.link = "";

    // console.log(this.file);
    if(!this.file) {
      alert("Upload Image.");
      return;
    }
    else {
      this.fileUploadService.upload(this.file).subscribe(
        response => {
          // console.log(response);
          // alert("Plant Name : " + response["payload"][0]["Plant Name"] +"\n" + "Plant Disease: " + response["payload"][0]["Plant Disease"] + "\n" + "Youtube Videos: " + "https://www.youtube.com/playlist?list=PLTHBCW2_RYXVBRFraxz3Es4HAuEE9uCaH");
          this.plantName = response["payload"][0]["Plant Name"];
          this.plantDisease = response["payload"][0]["Plant Disease"];
          this.cureSteps = response["payload"][0]["Cure Steps"];
          
          if(response["payload"][0]["Cure Steps"] == "No Cure.") {
            this.link = "";
          }
          else {
            this.link = "https://www.youtube.com/playlist?list=PLTHBCW2_RYXVBRFraxz3Es4HAuEE9uCaH";
          }
        }
      );
    }
  }

}
