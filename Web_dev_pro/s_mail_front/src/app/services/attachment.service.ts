import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Attachment} from "../models/attachment";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AttachmentService {

  private apiUrl = 'http://127.0.0.1:8000/api'; // Замените на ваш URL API

  constructor(private http: HttpClient) { }



  getAttachments(): Observable<Attachment[]> {
    return this.http.get<Attachment[]>(`${this.apiUrl}/mailbox/attachments/`);
  }

  // Создание нового вложения
  createAttachment(attachmentData: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/mailbox/mails/attachments/`, attachmentData);
  }

  // Получение деталей вложения по его идентификатору
  getAttachmentById(id: number): Observable<Attachment> {
    return this.http.get<Attachment>(`${this.apiUrl}/mailbox/mails/attachments/${id}/`);
  }

  // Удаление вложения по его идентификатору
  deleteAttachment(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/mailbox/mails/attachments/${id}/`);
  }
}
