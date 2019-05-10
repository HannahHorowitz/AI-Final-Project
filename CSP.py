# This CSP class is the basis for a generic Contraint Satisfaction Problem class
# Its intended use is to use as a base class to be overridden
# the function for consistent or chooseVariable can be overridden in a subclass

import copy

class CSP:

    def __init__ (self, variables, domains):
        # a list of variables
        # a dictionary of domains: a mapping of variables to a list of possible values
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0
        self.five = 0
        self.six = 0
        self.seven = 0
        self.eight = 0
        self.nine = 0
        self.ten = 0
        self.eleven = 0
        self.twelve = 0
        self.thirt = 0
        self.fourt = 0
        for v in variables:
            self.constraints[v] = []


    def addConstraint(self, variable1, variable2):
        # add a contaraint that variable 1 and variable 2 do not have the same value
        if variable2 not in self.constraints[variable1]:
            self.constraints[variable1].append(variable2)
        if variable1 not in self.constraints[variable2]:
            self.constraints[variable2].append(variable1)

    def ac3(self):
        # Arc-Consistancy 3
        # limits the domains of variables in the CSP that can't be satisfied
        arcs = []

        for variable1 in self.variables:
            for variable2 in self.constraints[variable1]:
                arcs.append((variable1, variable2))

        while len(arcs) > 0:
            arc = arcs.pop(0)
            variable1 = arc[0]
            if self.revise(variable1, arc[1]):
                if len(self.domains[variable1]) == 0:
                    return False

                for variable2 in self.constraints[variable1]:
                    if (variable2 != arc[1]):
                        arcs.append((variable2, variable1))
        return True


    def revise(self, variable1, variable2):
        # for each the values in the domain of variable 1
        # checks if there exists a value in variable2's domain the doesn't conflict
        # if no such value exists, remove the value from the domain of variable 1
        revised = False

        for val in self.domains[variable1]:
            satisfied = False

            for val2 in self.domains[variable2]:
                if val != val2:
                    satisfied = True

            if not satisfied:
                self.domains[variable1].remove(val)
                revised = True

        return revised


    def search(self):
        # use backtracking search to find a solution
        # updates the domains of each of the variables

        assignment = {}
        for variable in self.variables:
            if len(self.domains[variable]) == 1:
                assignment[variable] = self.domains[variable][0]

        solution = self.backtrack(assignment)

        if solution is not None:
            for variable in self.variables:
                self.domains[variable] = [solution[variable]]

    def solved(self):
        # return True if each variable has domain of lenth 1
        # and contraints are all not violated
        for variable in self.variables:
            if len(self.domains[variable]) != 1:
                return False
        return self.validateSolution()

    def validateSolution(self):
        # tests the contraints
        # if the value in the domain of a variable matchs the
        # value in a variable that is restricted by a constraint, return False
        # Otherwise; return True
        for variable1 in self.variables:
            for variable2 in self.constraints[variable1]:
                if self.domains[variable1][0] == self.domains[variable2][0]:
                    return False
        return True



    def consistent(self, variable, val, assignment):
        # inputs: a variable, a proposed value, and an assignment dictionary
        # returns False if assigning the val to the variable would conflict
        # with a constraint as another variable in the assignment is already assigned the val
        # otherwise, return True
        if val == 1:
            if self.one == 4:
                return False
        if val == 2:
            if self.two == 4:
                return False
        if val == 3:
            if self.three == 4:
                return False
        if val == 4:
            if self.four == 4:
                return False
        if val == 5:
            if self.five == 4:
                return False
        if val == 6:
            if self.six == 4:
                return False
        if val == 7:
            if self.seven == 4:
                return False
        if val == 8:
            if self.eight == 4:
                return False
        if val == 9:
            if self.nine == 4:
                return False
        if val == 10:
            if self.ten == 4:
                return False
        if val == 11:
            if self.eleven == 4:
                return False
        if val == 12:
            if self.twelve == 4:
                return False
        if val == 13:
            if self.thirt == 4:
                return False
        if val == 14:
            if self.fourt == 4:
                return False
        for variable2 in self.constraints[variable]:
            if variable2 in assignment and assignment[variable2] == val:
                return False
        return True

    def impossible(self):
        # returns True if the domain of any variable is empty -- no possible values
        # otherwise False
        for variable in self.variables:
            if len(self.domains[variable]) == 0:
                return True
        return False

    def backtrack(self, assignment):
        # input an assignment -- a dictionary between variables and a value
        # recursively search for a possible assignment that satisfies all contraints
        # returns an assignment mapping

        #TODO: Implement backtrack function here
        if len(assignment) == len(self.variables):
            return assignment

        variable = self.chooseVariable(assignment)
        for val in self.domains[variable]:
            if self.consistent(variable, val, assignment):
                new_assignment = copy.deepcopy(assignment)
                new_assignment[variable] = val
                # new_board = copy.deepcopy(self)
                self.domains[variable] = [val]
                if val == 1:
                    self.one +=1
                if val == 2:
                    self.two +=1
                if val == 3:
                    self.three +=1
                if val == 4:
                    self.four +=1
                if val == 5:
                    self.five +=1
                if val == 6:
                    self.six +=1
                if val == 7:
                    self.seven +=1
                if val== 8:
                    self.eight +=1
                if val== 9:
                    self.nine +=1
                if val== 10:
                    self.ten +=1
                if val== 11:
                    self.eleven +=1
                if val== 12:
                    self.twelve +=1
                if val== 13:
                    self.thirt +=1
                if val== 14:
                    self.fourt +=1
                #print(self.one)
                self.ac3()

                for v in self.variables:
                    if len(self.domains[v])== 1:
                        new_assignment[v] = self.domains[v][0]

                if not self.impossible():
                    result = self.backtrack(new_assignment)
                    if result is not None:
                        return result

        return None

    def chooseVariable(self, assignment):
        # return a variable that is not in the assignment
        for v in self.variables:
            if v not in assignment:
                return v
        return None


    def print(self, ):
        # print out each variable and its domain values
        result = ""
        for variable in self.variables:
            result += str(variable) + " : " + str(self.domains[variable]) + "\n"
        print(result)
