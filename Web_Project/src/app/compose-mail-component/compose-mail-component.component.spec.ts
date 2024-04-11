import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComposeMailComponentComponent } from './compose-mail-component.component';

describe('ComposeMailComponentComponent', () => {
  let component: ComposeMailComponentComponent;
  let fixture: ComponentFixture<ComposeMailComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ComposeMailComponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ComposeMailComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
