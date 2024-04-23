import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Message} from "./message";


@Injectable({
  providedIn: 'root'
})
export class MailService {

  private apiUrl = 'http://127.0.0.1:8000/api'; // Замените на ваш URL API

  constructor(private http: HttpClient) { }

  // Пример метода для получения списка входящих писем
  getInbox(): Observable<Message[]> {
    return this.http.get<Message[]>(`${this.apiUrl}/mailbox/mails/`);
  }
  getMailById(id: number): Observable<Message> {
    return this.http.get<Message>(`${this.apiUrl}/mailbox/mails/${id}/`);
  }
  // Пример метода для отправки нового письма
  sendMail(messageData: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/mailbox/mails/create/`, messageData);
  }

  // Добавьте другие методы для взаимодействия с вашим API, например, для работы с папками, вложениями и т.д.

}
