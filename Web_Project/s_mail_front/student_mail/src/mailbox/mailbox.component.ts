import {Component, OnInit} from '@angular/core';
import {MailService} from "../mail.service";
import {Message} from "../message";
import {Router} from "@angular/router";

@Component({
  selector: 'app-mailbox',
  // standalone: true,
  // imports: [],
  templateUrl: './mailbox.component.html',
  styleUrl: './mailbox.component.css'
})
export class MailboxComponent implements OnInit{
  inbox: Message[] = [];

  constructor(private router: Router, private mailService: MailService) { }

  ngOnInit(): void {
    this.loadInbox();
  }

  loadInbox() {
    this.mailService.getInbox().subscribe(data => {
      this.inbox = data;
    });
  }

  goToReadMail(id: number) {
    this.router.navigate(['/read', id]);
  }

  goToCompose() {
    this.router.navigate(['/compose']);
  }

  goToFolders() {
    this.router.navigate(['/folders']);
  }

  goToAttachments() {
    this.router.navigate(['/attachments']);
  }
}




