class InputBinding(Freezable,ISealable,ICommandSource):
 """
 Represents a binding between an System.Windows.Input.InputGesture and a command. The command is potentially a System.Windows.Input.RoutedCommand.
 
 InputBinding(command: ICommand,gesture: InputGesture)
 """
 def CloneCore(self,*args):
  """
  CloneCore(self: InputBinding,sourceFreezable: Freezable)
   Copies the base (non-animated) values of the properties of the specified object.
  
   sourceFreezable: The object to clone.
  """
  pass
 def CloneCurrentValueCore(self,*args):
  """
  CloneCurrentValueCore(self: InputBinding,sourceFreezable: Freezable)
   Copies the current values of the properties of the specified object.
  
   sourceFreezable: The object to clone.
  """
  pass
 def CreateInstance(self,*args):
  """
  CreateInstance(self: Freezable) -> Freezable
  
   Initializes a new instance of the System.Windows.Freezable class.
   Returns: The new instance.
  """
  pass
 def CreateInstanceCore(self,*args):
  """
  CreateInstanceCore(self: InputBinding) -> Freezable
  
   Creates an instance of an System.Windows.Input.InputBinding.
   Returns: The new object.
  """
  pass
 def FreezeCore(self,*args):
  """
  FreezeCore(self: Freezable,isChecking: bool) -> bool
  
   Makes the System.Windows.Freezable object unmodifiable or tests whether it can 
    be made unmodifiable.
  
  
   isChecking: true to return an indication of whether the object can be frozen (without 
    actually freezing it); false to actually freeze the object.
  
   Returns: If isChecking is true,this method returns true if the System.Windows.Freezable 
    can be made unmodifiable,or false if it cannot be made unmodifiable. If 
    isChecking is false,this method returns true if the if the specified 
    System.Windows.Freezable is now unmodifiable,or false if it cannot be made 
    unmodifiable.
  """
  pass
 def GetAsFrozenCore(self,*args):
  """
  GetAsFrozenCore(self: InputBinding,sourceFreezable: Freezable)
   Makes the instance a frozen clone of the specified System.Windows.Freezable by 
    using base (non-animated) property values.
  
  
   sourceFreezable: The object to clone.
  """
  pass
 def GetCurrentValueAsFrozenCore(self,*args):
  """
  GetCurrentValueAsFrozenCore(self: InputBinding,sourceFreezable: Freezable)
   Makes the current instance a frozen clone of the specified 
    System.Windows.Freezable. If the object has animated dependency properties,
    their current animated values are copied.
  
  
   sourceFreezable: The object to clone.
  """
  pass
 def OnChanged(self,*args):
  """
  OnChanged(self: Freezable)
   Called when the current System.Windows.Freezable object is modified.
  """
  pass
 def OnFreezablePropertyChanged(self,*args):
  """
  OnFreezablePropertyChanged(self: Freezable,oldValue: DependencyObject,newValue: DependencyObject,property: DependencyProperty)
   This member supports the Windows Presentation Foundation (WPF) infrastructure 
    and is not intended to be used directly from your code.
  
  
   oldValue: The previous value of the data member.
   newValue: The current value of the data member.
   property: The property that changed.
  OnFreezablePropertyChanged(self: Freezable,oldValue: DependencyObject,newValue: DependencyObject)
   Ensures that appropriate context pointers are established for a 
    System.Windows.DependencyObjectType data member that has just been set.
  
  
   oldValue: The previous value of the data member.
   newValue: The current value of the data member.
  """
  pass
 def OnPropertyChanged(self,*args):
  """
  OnPropertyChanged(self: Freezable,e: DependencyPropertyChangedEventArgs)
   Overrides the System.Windows.DependencyObject implementation of 
    System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
    rtyChangedEventArgs) to also invoke any System.Windows.Freezable.Changed 
    handlers in response to a changing dependency property of type 
    System.Windows.Freezable.
  
  
   e: Event data that contains information about which property changed,and its old 
    and new values.
  """
  pass
 def ReadPreamble(self,*args):
  """
  ReadPreamble(self: Freezable)
   Ensures that the System.Windows.Freezable is being accessed from a valid 
    thread. Inheritors of System.Windows.Freezable must call this method at the 
    beginning of any API that reads data members that are not dependency 
    properties.
  """
  pass
 def ShouldSerializeProperty(self,*args):
  """
  ShouldSerializeProperty(self: DependencyObject,dp: DependencyProperty) -> bool
  
   Returns a value that indicates whether serialization processes should serialize 
    the value for the provided dependency property.
  
  
   dp: The identifier for the dependency property that should be serialized.
   Returns: true if the dependency property that is supplied should be value-serialized; 
    otherwise,false.
  
  ShouldSerializeProperty(self: Window_16$17,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Label_17$18,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: TextBox_18$19,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Button_19$20,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: CheckBox_20$21,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: ComboBox_21$22,dp: DependencyProperty) -> bool
  ShouldSerializeProperty(self: Separator_22$23,dp: DependencyProperty) -> bool
  """
  pass
 def WritePostscript(self,*args):
  """
  WritePostscript(self: Freezable)
   Raises the System.Windows.Freezable.Changed event for the 
    System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged 
    method. Classes that derive from System.Windows.Freezable should call this 
    method at the end of any API that modifies class members that are not stored as 
    dependency properties.
  """
  pass
 def WritePreamble(self,*args):
  """
  WritePreamble(self: Freezable)
   Verifies that the System.Windows.Freezable is not frozen and that it is being 
    accessed from a valid threading context. System.Windows.Freezable inheritors 
    should call this method at the beginning of any API that writes to data members 
    that are not dependency properties.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,command,gesture):
  """
  __new__(cls: type)
  __new__(cls: type,command: ICommand,gesture: InputGesture)
  """
  pass
 Command=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Input.ICommand associated with this input binding.

Get: Command(self: InputBinding) -> ICommand

Set: Command(self: InputBinding)=value
"""

 CommandParameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the command-specific data for a particular command.

Get: CommandParameter(self: InputBinding) -> object

Set: CommandParameter(self: InputBinding)=value
"""

 CommandTarget=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the target element of the command.

Get: CommandTarget(self: InputBinding) -> IInputElement

Set: CommandTarget(self: InputBinding)=value
"""

 Gesture=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Input.InputGesture associated with this input binding.

Get: Gesture(self: InputBinding) -> InputGesture

Set: Gesture(self: InputBinding)=value
"""


 CommandParameterProperty=None
 CommandProperty=None
 CommandTargetProperty=None

