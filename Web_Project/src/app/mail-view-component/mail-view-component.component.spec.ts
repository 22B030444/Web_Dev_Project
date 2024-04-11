import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MailViewComponentComponent } from './mail-view-component.component';

describe('MailViewComponentComponent', () => {
  let component: MailViewComponentComponent;
  let fixture: ComponentFixture<MailViewComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MailViewComponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MailViewComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
