import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router'; // Импорт RouterModule
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MailboxComponent } from '../mailbox/mailbox.component';
import { MailsComponent } from '../mails/mails.component';
import { ReadMailsComponent } from '../read-mails/read-mails.component';
import { ComposeMailsComponent } from '../compose-mails/compose-mails.component';
import { FoldersComponent } from '../folders/folders.component';
import { AttachmentsComponent } from '../attachments/attachments.component';
import { LoginComponent } from '../login/login.component';
import { LogoutComponent } from '../logout/logout.component';
import { AuthInterceptor } from '../authinterceptor';
import { MailService } from '../mail.service';

@NgModule({
  declarations: [
    AppComponent,
    MailboxComponent,
    MailsComponent,
    ReadMailsComponent,
    ComposeMailsComponent,
    FoldersComponent,
    AttachmentsComponent,
    LoginComponent,
    LogoutComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot([]) // Используйте RouterModule.forRoot() здесь
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true },
    MailService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
