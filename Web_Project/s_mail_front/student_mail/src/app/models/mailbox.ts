import {User} from "./user";

export interface Mailbox {
  id: number;
  user: User; // ссылка на модель пользователя
  email_address: string;
  created_at: Date;

}
