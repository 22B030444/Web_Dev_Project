import {Component, OnInit} from '@angular/core';
import {MailService} from "../services/mail.service";
import {Message} from "../models/message";

@Component({
  selector: 'app-mails',
  // standalone: true,
  // imports: [],
  templateUrl: './mails.component.html',
  styleUrl: './mails.component.css'
})
export class MailsComponent implements OnInit{

  mails: Message [] = []

  constructor(private mailService: MailService) { }

  ngOnInit(): void {
    this.mailService.getInbox().subscribe(data => {
      this.mails = data;
    });
  }

}
