import {User} from "./user";
import {Folder} from "./folder";

export interface Message {
  id: number;
  subject: string;
  folder: Folder;
  body: string;
  sender: User; // ссылка на модель отправителя (пользователя)
  recipient: User; // ссылка на модель получателя (пользователя)
  send_at: Date;
  read: boolean; // или можно использовать enum для статусов

}
