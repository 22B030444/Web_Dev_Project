import {Component, OnInit} from '@angular/core';
import {Attachment} from "../../models/attachment";
import {AttachmentService} from "../../services/attachment.service";

@Component({
  selector: 'app-attachment-page',
  templateUrl: './attachment-page.component.html',
  styleUrls: ['./attachment-page.component.css']
})
export class AttachmentPageComponent implements OnInit{
  attachment: Attachment[] = []
  loading=false

  constructor(private attService: AttachmentService) {}

  ngOnInit() {
    this.loading=true;
    this.attService.getAttachments().subscribe((data)=>{
      this.loading = false
      this.attachment = data
    })
  }

}
