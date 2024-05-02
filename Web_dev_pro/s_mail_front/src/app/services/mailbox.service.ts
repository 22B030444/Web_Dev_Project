import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {AuthToken} from "../models/authToken";
import {Mailbox} from "../models/mailbox";

@Injectable({
  providedIn: 'root'
})
export class MailboxService {
  private URL = 'http://127.0.0.1:8000/api';
  constructor(private http: HttpClient) {}

  login(username: string, password: string): Observable<AuthToken> {
    return this.http.post<AuthToken>(`${this.URL}/login/`, {
      username,
      password,
    });
  }

  getMailBox(): Observable<Mailbox[]>{
    return this.http.get<Mailbox[]>(`${this.URL}/mailbox/`)
  }

}
