import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http'; // Если вы планируете использовать HTTP запросы

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
// Импортируйте все компоненты, которые вы создали

// Импортируйте сервисы, если они есть
import {MailboxComponent} from "../mailbox/mailbox.component";
import {MailsComponent} from "../mails/mails.component";
import {ReadMailsComponent} from "../read-mails/read-mails.component";
import {ComposeMailsComponent} from "../compose-mails/compose-mails.component";
import {FoldersComponent} from "../folders/folders.component";
import {AttachmentsComponent} from "../attachments/attachments.component";
import {MailService} from "../mail.service";
import {LoginComponent} from "../login/login.component";
import {FormsModule} from "@angular/forms";
import {AuthInterceptor} from "../authinterceptor";

@NgModule({
  declarations: [
    AppComponent,
    MailboxComponent,
    MailsComponent,
    ReadMailsComponent,
    ComposeMailsComponent,
    FoldersComponent,
    AttachmentsComponent,
    LoginComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    // Если вы планируете использовать HTTP запросы
  ],
  providers: [
    {provide: HTTP_INTERCEPTORS, useClass:AuthInterceptor, multi:true},
    // Укажите все сервисы, которые вы создали
    MailService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
