import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

import { RouterModule } from '@angular/router'; // Импорт RouterModule
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MailboxComponent } from './mailbox/mailbox.component';
import { MailsComponent } from './mails/mails.component';
import { ReadMailsComponent } from './read-mails/read-mails.component';
import { ComposeMailsComponent } from './compose-mails/compose-mails.component';
import { FoldersComponent } from './folders/folders.component';
import { AttachmentsComponent } from './attachments/attachments.component';

import { AuthInterceptor } from './authinterceptor';
import { MailService } from './services/mail.service';
import {FormsModule} from "@angular/forms";
// import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    MailboxComponent,
    MailsComponent,
    ReadMailsComponent,
    ComposeMailsComponent,
    FoldersComponent,
    AttachmentsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true },
    MailService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
