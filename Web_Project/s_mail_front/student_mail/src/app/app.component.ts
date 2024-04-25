import {Component, NgModule, OnInit} from '@angular/core';
import { AuthenticationService } from "./services/authentication.service";


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  title = 'Your Email Application';
  is_logged = false;
  username = '';
  pswd = '';

  constructor(private authService: AuthenticationService) {}

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.is_logged = true;
    }
  }

  login() {
    this.authService.login(this.username, this.pswd).subscribe((data) => {
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
