export interface User {
  id: number;
  username: string;
  email: string;
  password: string;
  registrationDate: Date;
  role: string; // или можно использовать enum для ролей
}
