import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  constructor(public navCtrl: NavController,public http: HttpClient) {
    this.postRequest();

  }

  postRequest(){

    let item = {
      id :58364494
    }
    console.log('Send : 58364494');
    this.http.post("http://localhost:50000/api", item)
    .subscribe((val) =>{
      console.log(' Receive : ' + val['item']);
    });
  }

}
