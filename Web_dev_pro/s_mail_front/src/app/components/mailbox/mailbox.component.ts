import {Component, Input} from '@angular/core';
import {Message} from "../../models/message";
import {Mailbox} from "../../models/mailbox";
import {Router} from "@angular/router";

@Component({
  selector: 'app-mailbox',
  templateUrl: './mailbox.component.html',
  styleUrls: ['./mailbox.component.css']
})
export class MailboxComponent {
  @Input() mailbox!: Mailbox;

  constructor(private router:Router) {}

  viewMails(mailbox: Mailbox){
    this.router.navigate(['/mailbox/' ]);
  }


}
