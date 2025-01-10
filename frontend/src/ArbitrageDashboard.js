import React, { useState, useEffect } from 'react';
import { ArrowUpDown, RefreshCcw, AlertCircle } from 'lucide-react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
//import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../../components/ui/card';


const ArbitrageDashboard = () => {
  const [opportunities, setOpportunities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [lastUpdate, setLastUpdate] = useState(null);

  // Fetch arbitrage data from backend API
  const fetchArbitrageData = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:5000/arbitrage');
      const data = await response.json();
      setOpportunities(data);
      setLastUpdate(new Date().toISOString());
    } catch (error) {
      console.error('Error fetching arbitrage data:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchArbitrageData();
    const interval = setInterval(fetchArbitrageData, 30000); // Refresh every 30 seconds
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="p-4 max-w-6xl mx-auto">
      <Card>
        <CardHeader>
          <div className="flex justify-between items-center">
            <div>
              <CardTitle>Arbitrage Scanner</CardTitle>
              <CardDescription>
                Real-time arbitrage opportunities between Binance and Solana DEX
              </CardDescription>
            </div>
            <button
              onClick={fetchArbitrageData}
              className="flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
              disabled={loading}
            >
              <RefreshCcw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
              Refresh
            </button>
          </div>
        </CardHeader>
        <CardContent>
          {loading ? (
            <div className="flex justify-center items-center h-48">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500" />
            </div>
          ) : (
            <>
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="border-b">
                      <th className="px-4 py-2 text-left">Token</th>
                      <th className="px-4 py-2 text-right">Binance Price</th>
                      <th className="px-4 py-2 text-right">Solana DEX Price</th>
                      <th className="px-4 py-2 text-right">Profit After Fees</th>
                    </tr>
                  </thead>
                  <tbody>
                    {opportunities.map((op, index) => (
                      <tr key={index} className="border-b hover:bg-gray-50">
                        <td className="px-4 py-2 font-medium">{op.pair}</td>
                        <td className="px-4 py-2 text-right">${op.binancePrice.toFixed(8)}</td>
                        <td className="px-4 py-2 text-right">${op.solanaPrice.toFixed(8)}</td>
                        <td className="px-4 py-2 text-right text-green-600">${op.profit.toFixed(8)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
              {lastUpdate && (
                <div className="mt-4 text-sm text-gray-500 flex items-center gap-2">
                  <AlertCircle className="w-4 h-4" />
                  Last updated: {new Date(lastUpdate).toLocaleTimeString()}
                </div>
              )}
            </>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default ArbitrageDashboard;
