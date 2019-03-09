import torch
import torch.nn.functional as F
from  torch.autograd import Variable
import matplotlib.pyplot as plt


n_data = torch.ones(100,2)
x0 = torch.normal(2*n_data,1)
y0 = torch.zeros(100)
x1 = torch.normal(-2*n_data,1)
y1 = torch.ones(100)
x = torch.cat((x0,x1),0).type(torch.FloatTensor)
y = torch.cat((y0,y1),).type(torch.LongTensor)

x,y = Variable(x),Variable(y)
#plt.scatter(x.data.numpy()[:,0],x.data.numpy()[:,1],c=y.data.numpy(),s=100,lw=0)
#plt.show()


class Net(torch.nn.Module):
    def __init__(self,n_feature,n_hidden,n_output):
        super(Net,self).__init__()
        self.hidden = torch.nn.Linear(n_feature,n_hidden)
        self.predict =torch.nn.Linear(n_hidden,n_output)

    def forward(self,x):
        x = F.relu(self.hidden(x))
        x = self.predict(x)
        return x


net = Net(2,10,2)

plt.ion()
plt.show()

optimizer = torch.optim.SGD(net.parameters(),lr=0.01)
loss_function = torch.nn.CrossEntropyLoss()

for t in range(100):
    out = net(x)

    loss = loss_function(out,y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if t% 2 == 0:
        plt.cla()
        prediction = torch.max(F.softmax(out),1)[1]
        pred_y = prediction.data.numpy().squeeze()
        target_y = y.data.numpy()
        plt.scatter(x.data.numpy()[:,0],x.data.numpy()[:,1],c=pred_y,s=100,lw=0)
        accuracy = sum(pred_y == target_y)*1.0/200
        plt.text(1.5,4,'Accuracy = %.2f ' % accuracy,fontdict={'size':20,'color':'red'})
        plt.pause(0.1)

plt.ioff()
plt.show()