import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MailListComponentComponent } from './mail-list-component.component';

describe('MailListComponentComponent', () => {
  let component: MailListComponentComponent;
  let fixture: ComponentFixture<MailListComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MailListComponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(MailListComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
