import {Mailbox} from "./mailbox";

export interface User {
  id: number;
  username: string;
  email: string;
  password: string;
  registrationDate: Date;
  role: string; // You might want to use an enum for roles instead of string
  mailbox: Mailbox; // Assuming Mailbox is another interface representing a user's mailbox
}
