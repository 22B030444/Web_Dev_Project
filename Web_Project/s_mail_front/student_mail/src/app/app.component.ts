import { Component, OnInit } from '@angular/core';
import {AuthenticationService} from "../authentication.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  title = 'head-hunter';
  is_logged = false;
  username = '';
  pswd = '';

  constructor(private authentication: AuthenticationService) {}

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.is_logged = true;
    }
  }

  login() {
    this.authentication.login(this.username, this.pswd).subscribe((data) => {
      localStorage.setItem('token', data.token);
      this.is_logged = true;
      this.username = '';
      this.pswd = '';
    });
  }
  logout() {
    this.is_logged = false;
    localStorage.removeItem('token');
  }
}
