import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MailboxComponent} from "./mailbox/mailbox.component";
import {ReadMailsComponent} from "./read-mails/read-mails.component";
import {ComposeMailsComponent} from "./compose-mails/compose-mails.component";
import {FoldersComponent} from "./folders/folders.component";
import {AttachmentsComponent} from "./attachments/attachments.component";
import {MailsComponent} from "./mails/mails.component";


const routes: Routes = [
  { path: '', redirectTo: 'mailbox', pathMatch: 'full' },
  { path: 'mails', component: MailsComponent },
  { path: 'read/:id', component: ReadMailsComponent },
  { path: 'compose', component: ComposeMailsComponent },
  { path: 'folders', component: FoldersComponent},
  { path: 'attachments', component: AttachmentsComponent },
  { path: 'mailbox', component: MailboxComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
