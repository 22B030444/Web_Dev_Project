import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {catchError, Observable, throwError} from 'rxjs';
import { Message } from "../models/message";
import { Attachment } from "../models/attachment";
import { Folder } from "../models/folder";


@Injectable({
  providedIn: 'root'
})
export class MailService {

  private apiUrl = 'http://127.0.0.1:8000/api'; // Замените на ваш URL API

  constructor(private http: HttpClient) { }
  getMailbox(): Observable<any> {
    const accessToken = localStorage.getItem('accessToken');
    if (!accessToken) {
      // Handle case when access token is not available
      return throwError('Access token is missing');
    }

    const headers = new HttpHeaders().set('Authorization', `Bearer ${accessToken}`);
    return this.http.get<any[]>(`${this.apiUrl}/mailbox/`, { headers }).pipe(
      catchError(error => {
        // Handle authentication error
        if (error.status === 401) {
          // Redirect to login page or handle the error as needed
          console.error('Authentication error:', error);
        }
        return throwError(error);
      })
    );
  }
  // Получение списка входящих писем
  getInbox(): Observable<Message[]> {
    return this.http.get<Message[]>(`${this.apiUrl}/mailbox/mails/`);
  }

  // Получение деталей письма по его идентификатору
  getMailById(id: number): Observable<Message> {
    return this.http.get<Message>(`${this.apiUrl}/mailbox/mails/${id}/`);
  }

  // Отправка нового письма
  sendMail(messageData: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/mailbox/mails/create/`, messageData);
  }

  // Удаление письма по его идентификатору
  deleteMail(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/mailbox/mails/${id}/`);
  }

  // Обновление письма по его идентификатору
  updateMail(id: number, mailData: any): Observable<Message> {
    return this.http.put<Message>(`${this.apiUrl}/mailbox/mails/${id}/`, mailData);
  }

  // Получение списка папок
  getFolders(): Observable<Folder[]> {
    return this.http.get<Folder[]>(`${this.apiUrl}/mailbox/folders/`);
  }

  // Получение деталей папки по ее идентификатору
  getFolderById(id: number): Observable<Folder> {
    return this.http.get<Folder>(`${this.apiUrl}/mailbox/folders/${id}/`);
  }

  // Создание новой папки
  createFolder(folderData: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/mailbox/folders/`, folderData);
  }

  // Удаление папки по ее идентификатору
  deleteFolder(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/mailbox/folders/${id}/`);
  }

  // Получение списка вложений
  getAttachments(): Observable<Attachment[]> {
    return this.http.get<Attachment[]>(`${this.apiUrl}/mailbox/mails/attachments/`);
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
