import React, { useState, useEffect } from 'react';
import { reportsAPI, alertsAPI } from '../services/api';
import { TrendingUp, Package, AlertTriangle, DollarSign, ShoppingCart } from 'lucide-react';

const Dashboard = () => {
  const [stats, setStats] = useState(null);
  const [alerts, setAlerts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [statsRes, alertsRes] = await Promise.all([
        reportsAPI.getDashboard(),
        alertsAPI.getAll(false)
      ]);
      setStats(statsRes.data);
      setAlerts(alertsRes.data);
    } catch (error) {
      console.error('Error fetching dashboard data:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="flex items-center justify-center h-full">Loading...</div>;
  }

  const statCards = [
    {
      title: 'Total Products',
      value: stats?.total_products || 0,
      icon: Package,
      color: 'bg-blue-500'
    },
    {
      title: 'Low Stock Items',
      value: stats?.low_stock_products || 0,
      icon: AlertTriangle,
      color: 'bg-red-500'
    },
    {
      title: 'Today\'s Revenue',
      value: `₹${(stats?.today_revenue || 0).toFixed(2)}`,
      icon: DollarSign,
      color: 'bg-green-500'
    },
    {
      title: 'Today\'s Profit',
      value: `₹${(stats?.today_profit || 0).toFixed(2)}`,
      icon: TrendingUp,
      color: 'bg-purple-500'
    },
    {
      title: 'Today\'s Sales',
      value: stats?.today_sales_count || 0,
      icon: ShoppingCart,
      color: 'bg-orange-500'
    },
    {
      title: 'Active Alerts',
      value: stats?.active_alerts || 0,
      icon: AlertTriangle,
      color: 'bg-yellow-500'
    }
  ];

  return (
    <div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        {statCards.map((stat, index) => {
          const Icon = stat.icon;
          return (
            <div key={index} className="bg-white rounded-lg shadow p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-gray-500 text-sm">{stat.title}</p>
                  <p className="text-2xl font-bold mt-2">{stat.value}</p>
                </div>
                <div className={`${stat.color} p-3 rounded-full text-white`}>
                  <Icon size={24} />
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {alerts.length > 0 && (
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold mb-4 flex items-center">
            <AlertTriangle className="mr-2 text-red-500" />
            Low Stock Alerts
          </h3>
          <div className="space-y-3">
            {alerts.map((alert) => (
              <div key={alert.id} className="flex items-center justify-between p-3 bg-red-50 rounded">
                <div>
                  <p className="font-medium">{alert.product_name}</p>
                  <p className="text-sm text-gray-600">
                    Current: {alert.current_stock} | Min Level: {alert.min_stock_level}
                  </p>
                </div>
                <button
                  onClick={() => {
                    alertsAPI.resolve(alert.id);
                    fetchData();
                  }}
                  className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600"
                >
                  Resolve
                </button>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
