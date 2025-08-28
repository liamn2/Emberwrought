class Cell:
    def __init__(self,dataTagType,compareAssignmentsMethod=None, serializeAssignmentMethod=None, deSerializeAssignmentMethod=None, dataDimension=1, optimizationCell = False, extendFromThisCell=True):
          self.mDataDimension = dataDimension
          self.mDataAssignmentPresent = False
          self.mDataAssignment = 0
          self.mExtendedAssignments = {}
          self.mDataTagType = dataTagType
          self.mOptimizationCell = optimizationCell
          self.mExtendFromThisCell = extendFromThisCell
          self.mBounds = [(None,None)] * self.mDataDimension
          self.mExtendedAssignmentConsistancyWeight = None
          if compareAssignmentsMethod==None:
             self.Compare = self.DefaultCompareAssignments
          else:
             self.Compare = compareAssignmentsMethod
          if serializeAssignmentMethod==None:
             self.mSerialize = self.DefaultSerialize
          else:
             self.mSerialize = serializeAssignmentMethod
          if deSerializeAssignmentMethod==None:
             self.mDeserialize = self.DefaultDeserialize
          else:
             self.mDeserialize = deSerializeAssignmentMethod
          return
    def SetDataAssignment(self, dataAssignment):
      if self.mDataTagType == dataAssignment.mValueType:
         self.mDataAssignmentPresent = True
         self.mDataAssignment = dataAssignment
      else:
         print("Cell::SetDataAssignment: Error, DataAssignment is of Incorrect type name. Expected:",self.mDataTagType,"Actual:",dataAssignment.mValueType)
      return # SetDataAssignment

   def SetCompareMethod(self, methodToSet):
      self.Compare = methodToSet
      return

       
