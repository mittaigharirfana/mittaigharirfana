import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowLeft, Save } from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Input } from '../../components/ui/input';
import { Label } from '../../components/ui/label';
import { toast } from '../../hooks/use-toast';

const AdminSettings = () => {
  const navigate = useNavigate();
  const [settings, setSettings] = useState({
    businessPhone: '8978152777',
    whatsappNumber: '8978152777',
    email: 'info@freshwala.com',
    address: 'Hyderabad, Telangana, India',
    facebookUrl: 'https://www.facebook.com/share/16NuCNAu5Y/?mibextid=wwXIfr',
    instagramUrl: 'https://www.instagram.com/freshwalam?igsh=MXd6cWVodXl2d2JtbA%3D%3D&utm_source=qr',
  });

  const handleChange = (e) => {
    setSettings({
      ...settings,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // In production, this would save to the database
    toast({
      title: 'Settings Saved',
      description: 'Your settings have been updated successfully. Note: Restart the app to see changes in header/footer.',
    });
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex items-center space-x-4 mb-8">
          <Button
            onClick={() => navigate('/admin/dashboard')}
            variant="outline"
            size="sm"
          >
            <ArrowLeft size={16} className="mr-2" />
            Back
          </Button>
          <h1 className="text-3xl font-bold text-gray-900">Settings</h1>
        </div>

        <div className="bg-white rounded-lg shadow-md p-6">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <h2 className="text-xl font-bold text-gray-900 mb-4">Contact Information</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <Label htmlFor="businessPhone">Business Phone</Label>
                  <Input
                    id="businessPhone"
                    name="businessPhone"
                    value={settings.businessPhone}
                    onChange={handleChange}
                    placeholder="+91 89781 52777"
                  />
                </div>
                <div>
                  <Label htmlFor="whatsappNumber">WhatsApp Number</Label>
                  <Input
                    id="whatsappNumber"
                    name="whatsappNumber"
                    value={settings.whatsappNumber}
                    onChange={handleChange}
                    placeholder="+91 89781 52777"
                  />
                </div>
                <div>
                  <Label htmlFor="email">Email Address</Label>
                  <Input
                    id="email"
                    name="email"
                    type="email"
                    value={settings.email}
                    onChange={handleChange}
                    placeholder="info@freshwala.com"
                  />
                </div>
                <div>
                  <Label htmlFor="address">Business Address</Label>
                  <Input
                    id="address"
                    name="address"
                    value={settings.address}
                    onChange={handleChange}
                    placeholder="Hyderabad, Telangana, India"
                  />
                </div>
              </div>
            </div>

            <div className="border-t pt-6">
              <h2 className="text-xl font-bold text-gray-900 mb-4">Social Media Links</h2>
              <div className="space-y-4">
                <div>
                  <Label htmlFor="facebookUrl">Facebook Page URL</Label>
                  <Input
                    id="facebookUrl"
                    name="facebookUrl"
                    value={settings.facebookUrl}
                    onChange={handleChange}
                    placeholder="https://facebook.com/freshwala"
                  />
                </div>
                <div>
                  <Label htmlFor="instagramUrl">Instagram Profile URL</Label>
                  <Input
                    id="instagramUrl"
                    name="instagramUrl"
                    value={settings.instagramUrl}
                    onChange={handleChange}
                    placeholder="https://instagram.com/freshwala"
                  />
                </div>
              </div>
            </div>

            <div className="border-t pt-6">
              <h2 className="text-xl font-bold text-gray-900 mb-4">Current Settings</h2>
              <div className="bg-gray-50 rounded-lg p-4 space-y-2 text-sm">
                <p><strong>Business Phone:</strong> {settings.businessPhone}</p>
                <p><strong>WhatsApp:</strong> {settings.whatsappNumber}</p>
                <p><strong>Email:</strong> {settings.email}</p>
                <p><strong>Address:</strong> {settings.address}</p>
                <p><strong>Facebook:</strong> <a href={settings.facebookUrl} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">View Page</a></p>
                <p><strong>Instagram:</strong> <a href={settings.instagramUrl} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">View Profile</a></p>
              </div>
            </div>

            <div className="flex justify-end">
              <Button type="submit" className="bg-orange-500 hover:bg-orange-600">
                <Save size={16} className="mr-2" />
                Save Settings
              </Button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default AdminSettings;
