import {User} from "./user";

export interface Mailbox {
  id: number;
  user: User;
  email_address: string;
  created_at: Date;

}
