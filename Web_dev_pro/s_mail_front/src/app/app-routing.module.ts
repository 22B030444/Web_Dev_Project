import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import {MailboxPageComponent} from "./pages/mailbox-page/mailbox-page.component";
import {MailPageComponent} from "./pages/mail-page/mail-page.component";
import {FolderPageComponent} from "./pages/folder-page/folder-page.component";
import {AttachmentPageComponent} from "./pages/attachment-page/attachment-page.component";

const routes: Routes = [
  { path: 'mailbox', component: MailboxPageComponent },
  { path: 'mails/:id', component: MailPageComponent },
  { path: 'folders', component: FolderPageComponent },
  { path: 'folders/:id', component: FolderPageComponent },
  { path: 'attachments', component: AttachmentPageComponent},
  { path: '', redirectTo: 'mailbox', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
