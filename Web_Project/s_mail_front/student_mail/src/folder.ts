import {Mailbox} from "./mailbox";
import {User} from "./user";

export interface Folder {
  id: number;
  name: string;
  mailbox: Mailbox; // Идентификатор почтового ящика, к которому относится папка
  user: User; // Идентификатор пользователя, к которому относится папка
  folderType: string; // Тип папки (например, Inbox, Sent, Drafts и т.д.)
}
