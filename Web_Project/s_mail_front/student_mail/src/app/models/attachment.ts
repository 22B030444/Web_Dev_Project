import {Message} from "./message";

export interface Attachment {
  id: number;
  file: File; // ссылка на файл
  filename: string;
  size: number;
  message: Message; // ссылка на модель сообщения
}
