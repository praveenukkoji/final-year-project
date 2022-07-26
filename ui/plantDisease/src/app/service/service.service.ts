import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

import { Response } from '../model/Response'

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  // API url
  baseApiUrl = "http://127.0.0.1:8000/predict/"

  constructor(private http:HttpClient) { }

  // Returns an observable
  upload(file: any):Observable<any> {
  
    // Create form data
    const formData = new FormData(); 

    // Store form name as "file" with file data
    formData.append("imgFile", file, file.name);
      
    // Make http post request over api
    // with formData as req
    return this.http.post<Response>(this.baseApiUrl, formData)
  }
}
