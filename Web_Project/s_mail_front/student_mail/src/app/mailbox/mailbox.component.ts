import { Component, OnInit } from '@angular/core';
import {MailService} from "../services/mail.service";


@Component({
  selector: 'app-mailbox',
  templateUrl: './mailbox.component.html',
  styleUrls: ['./mailbox.component.css']
})
export class MailboxComponent implements OnInit {

  mailboxData: any; // Define a variable to store mailbox data

  constructor(private mailboxService: MailService) { }

  ngOnInit(): void {
    // Call the method to fetch mailbox data when the component initializes
    this.getMailboxData();
  }

  getMailboxData(): void {
    // Call the service method to fetch mailbox data
    this.mailboxService.getMailbox()
      .subscribe(
        (data) => {
          // Assign the fetched data to the mailboxData variable
          this.mailboxData = data;
        },
        (error) => {
          console.error('Error fetching mailbox data:', error);
          // Handle error here, e.g., show an error message to the user
        }
      );
  }

}
